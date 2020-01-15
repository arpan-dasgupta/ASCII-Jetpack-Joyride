import numpy as numpy


def check(corners, point):
    # print(corners, point)
    if point[0] >= corners[0][0] and point[0] <= corners[1][0] and point[1] >= corners[0][1] and point[1] <= corners[1][1]:
        return True
    return False


def collision_checker(body1_dim, body2_dim, body1_pos, body2_pos):
    corners = [body1_pos, [body1_pos[0] +
                           body1_dim[0]-1, body1_pos[1]+body1_dim[1]-1]]
    bool_val = False
    # for i in range(body2_dim[0]):
    #     bool_val = bool_val or check(corners, [
    #                                  body2_pos[0]+i, body2_pos[1]]) or check(corners, [body2_pos[0]+i, body2_pos[1]+body2_dim[1]-1])
    #     if bool_val:
    #         break
    # for i in range(body2_dim[1]):
    #     bool_val = bool_val or check(corners, [
    #                                  body2_pos[0], body2_pos[1]+i]) or check(corners, [body2_pos[0]+body2_dim[0]-1, body2_pos[1]+i])
    #     if bool_val:
    #         break
    for i in range(body2_dim[0]):
        for j in range(body2_dim[1]):
            bool_val = bool_val or check(
                corners, [body2_pos[0]+i, body2_pos[1]+j])
            if bool_val:
                break
    # if check(corners, body2_pos) or check(corners, [body2_pos[0]+body2_dim[0]-1, body2_pos[1]]) or check(corners, [body2_pos[0]+body2_dim[0]-1, body2_pos[1]+body2_dim[1]-1]) or check(corners, [body2_pos[0], body2_pos[1]+body2_dim[1]-1]):
    #     res = True
    # else:
    #     res = False
    # fd = open("log.txt", 'a')
    # fd.write(str(corners)+' '+str(body2_pos) +
    #          ' '+str(body2_dim)+' '+str(bool_val)+'\n')
    # fd.close()
    return bool_val


if __name__ == '__main__':
    print(collision_checker([3, 3], [2, 3], [1, 0], [0, 2]))
    print(collision_checker([3, 3], [2, 3], [1, 0], [0, 2]))
