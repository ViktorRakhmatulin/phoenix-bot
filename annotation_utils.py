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
                              tag_size=48.0)
    # print(results)

    if not results:
        print('apriltag not found')
        return
    return results

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
    
    return keypoints, anchors

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

# def apply_wart_tf(warp_tf,kpts):

def show_image_with_points(img, points, comment):
    for c in points:
        kc = int(c[0]), int(c[1])
        cv2.circle(img, kc, 3, (0,255, 255), -1)
    cv2.imshow(comment, img)
    cv2.waitKey(0)
    # cv2.imwrite(comment+".jpg", img)
