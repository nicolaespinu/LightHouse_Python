# Challenge¶
# Dot has a lot of different boxes laying around. They need a system for how to unpack them,
# or they'll just continue procrastinating. Help Dot sort the boxes by their weight.
#
# Box:	Weight (kg)
# Box 1	4
# Box 2	2
# Box 3	18
# Box 4	21
# Box 5	14
# Box 6	13
# Create a function that will open the boxes according to their weight, from lightest to heaviest
# example dictionary
user_boxes = {'weight': [4, 2, 18, 21, 14, 13],
              'box_name': ['box1', 'box2', 'box3', 'box4', 'box5', 'box6']
              }
weight = user_boxes.pop('weight');
box_name = user_boxes.pop('box_name');


# print(weight);
# print(box_name);


def unpackBoxes(weight, box_name):
    result = {};
    sorted_dict = {}
    result_list = []

    for i in range(len(weight)):
        result[weight[i]] = box_name[i]
    sorted_dict = sorted(result.items());
    for i in range(len(sorted_dict)):
        result_list.append(sorted_dict.__getitem__(i)[1])
    return result_list;


print(unpackBoxes(weight, box_name));
