import dt_apriltags as apriltag
import cv2
import numpy as np
from skimage.transform import ProjectiveTransform, warp
from skimage import transform
from scipy.spatial.transform import Rotation as R

detector = apriltag.Detector(families="tagStandard52h13")


def detect_apriltag(img,camera_params):
    """
    returns detection object, containing marker center and corners coordinates 
    """
    if isinstance(img, str):
        print('reading img from file system')
        img = cv2.imread(img)
    if not type(img[0][0][0]) == np.uint8:
        img = img/img.max()
        img *= 255
        img = img.astype(np.uint8)
#         cv2.imshow('detect_apriltag', img)
        cv2.waitKey(1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    results = detector.detect(gray,
                              estimate_tag_pose=True,
                              camera_params=camera_params, 
                              tag_size=0.048)
    if not results:
        print('apriltag not found')
        return
    return results


def get_projection(c_to, c_from):
    """
    returns projection matrix by points provided
    """
    tform = ProjectiveTransform()
    tform.estimate(c_to, c_from)
    return tform

def get_straight_corners(res):
    """
    normalizes corners to form a square, returns new corners' coords
    """
    corners = [r for r in res if r.tag_id==48701][0].corners
    
    corners[:2] = np.array(sorted(corners[:2], key=lambda x: x[1]))
    corners[2:] = np.array(sorted(corners[2:], key=lambda x: x[1]))

    a = corners[:2][:, 0].mean()
    c = corners[2:][:, 0].mean()
    b = corners[::2][:, 1].mean()
    d = corners[1::2][:, 1].mean()
    
    desired_corners = np.array([[a, b], [a, d], [c, b], [c, d]], dtype=int)
    return desired_corners

def get_keypoints_on_image(img, corrected_normalized_keypoints,camera_params):
    """
    detects keypoints on image, with image warp and all the stuff, 
    returns points' coords on original image 
    """
    res = detect_apriltag(img,camera_params)
    img_warped, desired_corners,tform = warp_img(img, res)
    res_warp = detect_apriltag(img_warped,camera_params)
    warped_keypoints = get_keypoints_on_warped_image(res_warp, corrected_normalized_keypoints)
    desired_corners = get_straight_corners(res_warp)
#     print("desired_corners", desired_corners)
    str_project = get_projection(desired_corners, res[0].corners)
    print(str_project.params)
    points_on_image = [str_project.params @ np.array([p[0], p[1], 1]) for p in warped_keypoints]
    for p in points_on_image:
        p/= p[2]
    
    return np.array(points_on_image)
 
def warp_img(image, res):
    """warps image so marker would be square"""
    desired_corners = get_straight_corners(res)

    tform = get_projection(desired_corners, res[0].corners)
    image_warped = warp(image, tform)
    return image_warped, desired_corners, tform

def draw_corners(img, r, show=False):
    """draws marker corners, returns them"""
    if isinstance(r, np.ndarray):
        imagePoints = [r]
    else:
        imagePoints = r.corners.reshape(1,4,2)
    
    for corner in range(np.size(imagePoints[0],axis=0)):
        center = ((int(imagePoints[0][corner][0]),int(imagePoints[0][corner][1])))
        cv2.circle(img, center, 3, (0,0,255), -1)
    
    if show:
        cv2.imshow('img', color_image)
    return imagePoints[0]

def get_points_from_CAD():
    # we consider that marker has 40 mm length
# keypoints are defined from the CAD data
    """
    defines keypoints and holes' centers in marker CS
    """
    keypoints = np.zeros((14,2))
    i = 0
    keypoints[2*i] = [6.143, 37.51]
    keypoints[2*i+1] = [-keypoints[2*i][0], keypoints[2*i][1]]
    i+=1
    keypoints[2*i] = [27.213, 28.666]
    keypoints[2*i+1] = [-keypoints[2*i][0], keypoints[2*i][1]]
    i+=1
    keypoints[2*i] = [13.161, 26.86]
    keypoints[2*i+1] = [-keypoints[2*i][0], keypoints[2*i][1]]
    i+=1
    keypoints[2*i] = [27.707, 19.26]
    keypoints[2*i+1] = [-keypoints[2*i][0], keypoints[2*i][1]]
    i+=1
    keypoints[2*i] = [38.253, 5.53]
    keypoints[2*i+1] = [-keypoints[2*i][0], keypoints[2*i][1]]
    i+=1
    keypoints[2*i] = [19.9, -27.273]
    keypoints[2*i+1] = [-keypoints[2*i][0], keypoints[2*i][1]]
    i+=1
    keypoints[2*i] = [20.4, -29.39]
    keypoints[2*i+1] = [-keypoints[2*i][0], keypoints[2*i][1]]
    i+=1

    anchors = np.zeros((7,3))

    anchors[0] = [0.0, 0.0, 2.25]
    anchors[1] = [8.0, 11.2, 2.25]
    anchors[2] = anchors[1].copy()
    anchors[2][0] *= -1
    anchors[3] = [16.0, 0, 2.25]
    anchors[4] = anchors[3].copy()
    anchors[4][0] *= -1
    anchors[5] = [8.0, -13.86, 2.25]
    anchors[6] = anchors[5].copy()
    anchors[6][0] *= -1
    
    return keypoints, anchors[:,:2]

def rot_mtx(theta):
    """
    rotation matrix for 2D coords
    """
    rot = np.eye(2)
    rot[0,0] = np.cos(theta)
    rot[0,1] = -np.sin(theta)
    rot[1,0] = np.sin(theta)
    rot[1,1] = np.cos(theta)
    return rot

def normalize_and_orient_kpts(points_in_CAD):
    def correct_CAD_kpts_orientation(points_in_CAD):
        rot = rot_mtx(np.deg2rad(180))
        for i,kp in enumerate(points_in_CAD):
            points_in_CAD[i] = rot @ kp
        return points_in_CAD
    
    points_normalized = points_in_CAD/48

    points_normalized = correct_CAD_kpts_orientation(points_normalized)
    
    return points_normalized

def draw_points_on_aruco(img, res, keypoints, show=False):
    
    dx = (res[0].corners[2] - res[0].corners[1])
    dy = (res[0].corners[2] - res[0].corners[3])
    center = (res[0].corners[1] + res[0].corners[3])/2
    normality_check = dx@dy/(np.linalg.norm(dx)*np.linalg.norm(dy))
    scale = dx[0] 
    scaled_keypoints = kp_copy * scale + center

    if show:
#         draw_corners(img, res[0])
        for p in scaled_keypoints:
            kp = int(p[0]), int(p[1])
            cv2.circle(img, kp, 2, (0, 0, 255), -1)
        cv2.imshow('draw_points_on_aruco', img)
        cv2.waitKey(0)
    return scaled_keypoints

def get_corrected_normalized_keypoints(res_warp,
                                        anchors_points_normalized,
                                        anchor_ground_truth,
                                        normalized_keypoints):
    

    def get_corrective_tf(anchor_marker, anchor_gt):
        corrective_tf = cv2.estimateAffine2D(anchor_marker, anchor_gt,ransacReprojThreshold = 2)
        return corrective_tf
    
    anchors_points = get_keypoints_on_warped_image(res_warp, anchors_points_normalized)
    keypoints = get_keypoints_on_warped_image(res_warp, normalized_keypoints)
    # print(keypoints)
    corrective_tf, inliers = get_corrective_tf(anchors_points,anchor_ground_truth)
    
#     tform = ProjectiveTransform()
    tform = transform.estimate_transform('euclidean', anchor_ground_truth, anchors_points)
#     tform.estimate('euclidean',anchors_points,anchor_ground_truth)
    print("tform.params")
    print(tform.params)
    print("resulting transform to correct points")
    print(corrective_tf)
    print("inliers", inliers)
    dx = (res_warp[0].corners[2] - res_warp[0].corners[1])
    center = (res_warp[0].corners[1] + res_warp[0].corners[3])/2
    scale = dx[0]
    homog_keypoints = np.hstack((keypoints,np.ones((keypoints.shape[0],1))))
    # corrective_tf = tform.params
    corrected_points =(corrective_tf @ homog_keypoints.T).T
    print(corrected_points)
    # print((corrective_tf @ homog_keypoints.T).T)
    transformed_anchors_points = (corrective_tf @  np.hstack((anchors_points,np.ones((anchors_points.shape[0],1)))).T).T
#     for p in corrected_points:
# #         print(p)
#         p/=p[2]
    
    corrected_normalized_kpts =  (corrected_points - center)/ scale

    return corrected_points, corrected_normalized_kpts,transformed_anchors_points


def get_keypoints_on_warped_image(res_warp, normalized_kpts):
    dx = (res_warp[0].corners[2] - res_warp[0].corners[1])
    center = (res_warp[0].corners[1] + res_warp[0].corners[3])/2
    scale = dx[0] 
    keypoints = normalized_kpts * scale + center
    
    return keypoints


def show_save_image_with_points(img, points, comment):
    for c in points:
        kc = int(c[0]), int(c[1])
        cv2.circle(img, kc, 3, (0,255, 255), -1)
    cv2.imshow(comment, img)
    cv2.waitKey(0)
    cv2.imwrite(comment+".jpg", img)
