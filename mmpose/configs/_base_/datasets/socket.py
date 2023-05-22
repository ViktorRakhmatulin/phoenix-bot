dataset_info = dict(
    dataset_name='socket',
    paper_info=dict(
        author='Lin, Tsung-Yi and Maire, Michael and '
        'Belongie, Serge and Hays, James and '
        'Perona, Pietro and Ramanan, Deva and '
        r'Doll{\'a}r, Piotr and Zitnick, C Lawrence',
        title='Microsoft coco: Common objects in context',
        container='European conference on computer vision',
        year='2014',
        homepage='http://cocodataset.org/',
    ),
    keypoint_info={
        0:
        dict(
        name='zero',
         id=0,
          color=[51, 153, 255],
           type='upper',
            swap='one'),
        1:
        dict(
            name='one',
            id=1,
            color=[51, 153, 255],
            type='upper',
            swap='zero'),
        2:
        dict(
            name='two',
            id=2,
            color=[51, 153, 255],
            type='upper',
            swap='three'),
        3:
        dict(
            name='three',
            id=3,
            color=[51, 153, 255],
            type='upper',
            swap='two'),
        4:
        dict(
            name='four',
            id=4,
            color=[51, 153, 255],
            type='upper',
            swap='five'),
        5:
        dict(
            name='five',
            id=5,
            color=[0, 255, 0],
            type='upper',
            swap='four'),
        6:
        dict(
            name='six',
            id=6,
            color=[255, 128, 0],
            type='upper',
            swap='seven'),
        7:
        dict(
            name='seven',
            id=7,
            color=[0, 255, 0],
            type='upper',
            swap='six'),
        8:
        dict(
            name='eight',
            id=8,
            color=[255, 128, 0],
            type='upper',
            swap='nine'),
        9:
        dict(
            name='nine',
            id=9,
            color=[0, 255, 0],
            type='upper',
            swap='eight'),
        10:
        dict(
            name='ten',
            id=10,
            color=[255, 128, 0],
            type='upper',
            swap='eleven'),
        11:
        dict(
            name='eleven',
            id=11,
            color=[0, 255, 0],
            type='lower',
            swap='ten'),
        12:
        dict(
            name='twelve',
            id=12,
            color=[255, 128, 0],
            type='lower',
            swap='thirteen'),
        13:
        dict(
            name='thirteen',
            id=13,
            color=[0, 255, 0],
            type='lower',
            swap='twelve')
        },
    skeleton_info={
        0:
	dict(link=('zero', 'one'), id=0, color=[0,255,0]),
	1:
	dict(link=('zero', 'two'), id=1, color=[0,255,0]),
	2:
	dict(link=('zero', 'three'), id=2, color=[0,255,0]),
	3:
	dict(link=('zero', 'four'), id=3, color=[0,255,0]),
	4:
	dict(link=('zero', 'five'), id=4, color=[0,255,0]),
	5:
	dict(link=('zero', 'six'), id=5, color=[0,255,0]),
	6:
	dict(link=('zero', 'seven'), id=6, color=[0,255,0]),
	7:
	dict(link=('zero', 'eight'), id=7, color=[0,255,0]),
	8:
	dict(link=('zero', 'nine'), id=8, color=[0,255,0]),
	9:
	dict(link=('zero', 'ten'), id=9, color=[0,255,0]),
	10:
	dict(link=('zero', 'eleven'), id=10, color=[0,255,0]),
	11:
	dict(link=('zero', 'twelve'), id=11, color=[0,255,0]),
	12:
	dict(link=('zero', 'thirteen'), id=12, color=[0,255,0]),
	13:
	dict(link=('one', 'two'), id=13, color=[0,255,0]),
	14:
	dict(link=('one', 'three'), id=14, color=[0,255,0]),
	15:
	dict(link=('one', 'four'), id=15, color=[0,255,0]),
	16:
	dict(link=('one', 'five'), id=16, color=[0,255,0]),
	17:
	dict(link=('one', 'six'), id=17, color=[0,255,0]),
	18:
	dict(link=('one', 'seven'), id=18, color=[0,255,0]),
	19:
	dict(link=('one', 'eight'), id=19, color=[0,255,0]),
	20:
	dict(link=('one', 'nine'), id=20, color=[0,255,0]),
	21:
	dict(link=('one', 'ten'), id=21, color=[0,255,0]),
	22:
	dict(link=('one', 'eleven'), id=22, color=[0,255,0]),
	23:
	dict(link=('one', 'twelve'), id=23, color=[0,255,0]),
	24:
	dict(link=('one', 'thirteen'), id=24, color=[0,255,0]),
	25:
	dict(link=('two', 'three'), id=25, color=[0,255,0]),
	26:
	dict(link=('two', 'four'), id=26, color=[0,255,0]),
	27:
	dict(link=('two', 'five'), id=27, color=[0,255,0]),
	28:
	dict(link=('two', 'six'), id=28, color=[0,255,0]),
	29:
	dict(link=('two', 'seven'), id=29, color=[0,255,0]),
	30:
	dict(link=('two', 'eight'), id=30, color=[0,255,0]),
	31:
	dict(link=('two', 'nine'), id=31, color=[0,255,0]),
	32:
	dict(link=('two', 'ten'), id=32, color=[0,255,0]),
	33:
	dict(link=('two', 'eleven'), id=33, color=[0,255,0]),
	34:
	dict(link=('two', 'twelve'), id=34, color=[0,255,0]),
	35:
	dict(link=('two', 'thirteen'), id=35, color=[0,255,0]),
	36:
	dict(link=('three', 'four'), id=36, color=[0,255,0]),
	37:
	dict(link=('three', 'five'), id=37, color=[0,255,0]),
	38:
	dict(link=('three', 'six'), id=38, color=[0,255,0]),
	39:
	dict(link=('three', 'seven'), id=39, color=[0,255,0]),
	40:
	dict(link=('three', 'eight'), id=40, color=[0,255,0]),
	41:
	dict(link=('three', 'nine'), id=41, color=[0,255,0]),
	42:
	dict(link=('three', 'ten'), id=42, color=[0,255,0]),
	43:
	dict(link=('three', 'eleven'), id=43, color=[0,255,0]),
	44:
	dict(link=('three', 'twelve'), id=44, color=[0,255,0]),
	45:
	dict(link=('three', 'thirteen'), id=45, color=[0,255,0]),
	46:
	dict(link=('four', 'five'), id=46, color=[0,255,0]),
	47:
	dict(link=('four', 'six'), id=47, color=[0,255,0]),
	48:
	dict(link=('four', 'seven'), id=48, color=[0,255,0]),
	49:
	dict(link=('four', 'eight'), id=49, color=[0,255,0]),
	50:
	dict(link=('four', 'nine'), id=50, color=[0,255,0]),
	51:
	dict(link=('four', 'ten'), id=51, color=[0,255,0]),
	52:
	dict(link=('four', 'eleven'), id=52, color=[0,255,0]),
	53:
	dict(link=('four', 'twelve'), id=53, color=[0,255,0]),
	54:
	dict(link=('four', 'thirteen'), id=54, color=[0,255,0]),
	55:
	dict(link=('five', 'six'), id=55, color=[0,255,0]),
	56:
	dict(link=('five', 'seven'), id=56, color=[0,255,0]),
	57:
	dict(link=('five', 'eight'), id=57, color=[0,255,0]),
	58:
	dict(link=('five', 'nine'), id=58, color=[0,255,0]),
	59:
	dict(link=('five', 'ten'), id=59, color=[0,255,0]),
	60:
	dict(link=('five', 'eleven'), id=60, color=[0,255,0]),
	61:
	dict(link=('five', 'twelve'), id=61, color=[0,255,0]),
	62:
	dict(link=('five', 'thirteen'), id=62, color=[0,255,0]),
	63:
	dict(link=('six', 'seven'), id=63, color=[0,255,0]),
	64:
	dict(link=('six', 'eight'), id=64, color=[0,255,0]),
	65:
	dict(link=('six', 'nine'), id=65, color=[0,255,0]),
	66:
	dict(link=('six', 'ten'), id=66, color=[0,255,0]),
	67:
	dict(link=('six', 'eleven'), id=67, color=[0,255,0]),
	68:
	dict(link=('six', 'twelve'), id=68, color=[0,255,0]),
	69:
	dict(link=('six', 'thirteen'), id=69, color=[0,255,0]),
	70:
	dict(link=('seven', 'eight'), id=70, color=[0,255,0]),
	71:
	dict(link=('seven', 'nine'), id=71, color=[0,255,0]),
	72:
	dict(link=('seven', 'ten'), id=72, color=[0,255,0]),
	73:
	dict(link=('seven', 'eleven'), id=73, color=[0,255,0]),
	74:
	dict(link=('seven', 'twelve'), id=74, color=[0,255,0]),
	75:
	dict(link=('seven', 'thirteen'), id=75, color=[0,255,0]),
	76:
	dict(link=('eight', 'nine'), id=76, color=[0,255,0]),
	77:
	dict(link=('eight', 'ten'), id=77, color=[0,255,0]),
	78:
	dict(link=('eight', 'eleven'), id=78, color=[0,255,0]),
	79:
	dict(link=('eight', 'twelve'), id=79, color=[0,255,0]),
	80:
	dict(link=('eight', 'thirteen'), id=80, color=[0,255,0]),
	81:
	dict(link=('nine', 'ten'), id=81, color=[0,255,0]),
	82:
	dict(link=('nine', 'eleven'), id=82, color=[0,255,0]),
	83:
	dict(link=('nine', 'twelve'), id=83, color=[0,255,0]),
	84:
	dict(link=('nine', 'thirteen'), id=84, color=[0,255,0]),
	85:
	dict(link=('ten', 'eleven'), id=85, color=[0,255,0]),
	86:
	dict(link=('ten', 'twelve'), id=86, color=[0,255,0]),
	87:
	dict(link=('ten', 'thirteen'), id=87, color=[0,255,0]),
	88:
	dict(link=('eleven', 'twelve'), id=88, color=[0,255,0]),
	89:
	dict(link=('eleven', 'thirteen'), id=89, color=[0,255,0]),
	90:
	dict(link=('twelve', 'thirteen'), id=90, color=[0,255,0])
    },
    joint_weights=[1.]*14,
    sigmas=[0.026]*14)
