
# 836. Rectangle Overlap
class Solution:
    def isRectangleOverlap(self, rec1, rec2):

        if rec1[0] > rec2[0]:
            rec1, rec2 = rec2, rec1

        print(f"rec1[1] ={rec1[1]}, rec2[1]={rec2[1]}, rec1[3]={rec1[3]}")
        if rec1[0] <= rec2[0] < rec1[2] and \
                (rec1[1] <= rec2[1] < rec1[3] or  (rec2[1] <= rec1[1] and rec2[3] > rec1[1]) ):
            return True

        return False

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

rec1=[7,8,13,15]
rec2=[10,8,12,20]

# rec1=[11,12,13,13]
# rec2=[17,1,17,19]

# rec1=[-7,-3,10,5]
# rec2=[-6,-5,5,10]
rec1=[4,4,14,7]
rec2=[4,3,8,8]
rec1=[-382,-696,838,-517]
rec2=[-110,-690,247,-209]
obj = Solution()
print(obj.isRectangleOverlap(rec1, rec2))

# if rec1[0] >= rec2[2]: return False
# if rec1[2] <= rec2[0]: return False
# if rec1[1] >= rec2[3]: return False
# if rec1[3] <= rec2[1]: return False
#
# return True