import numpy as numpy


def check(corners, point):
    # print(corners, point)
    if point[0] >= corners[0][0] and point[0] <= corners[1][0] and point[1] >= corners[0][1] and point[1] <= corners[1][1]:
        return True
    return False


def collision_checker(body1_dim, body2_dim, body1_pos, body2_pos):
    corners = [body1_pos, [body1_pos[0] +
                           body1_dim[0]-1, body1_pos[1]+body1_dim[1]-1]]
    if check(corners, body2_pos) or check(corners, [body2_pos[0]+body2_dim[0]-1, body2_pos[1]]) or check(corners, [body2_pos[0]+body2_dim[0]-1, body2_pos[1]+body2_dim[1]-1]) or check(corners, [body2_pos[0], body2_pos[1]+body2_dim[1]-1]):
        return True
    return False


if __name__ == '__main__':
    print(collision_checker([3, 3], [2, 3], [1, 0], [0, 2]))
