from libcpp.vector cimport vector

cdef extern from "Solution.hpp":
    cdef cppclass Solution:
        Solution() except +
        void rotate(vector[int]& num, int k)

cdef class cppSolution:
    cdef Solution* thisptr

    def __cinit__(self):
        self.thisptr = new Solution()
    
    def __dealloc__(self):
        del self.thisptr
    
    def rotate(self, nums, int k):
        cdef vector[int] cpp_arr
        cdef int i

        for i in nums:
            cpp_arr.push_back(i)
        
        self.thisptr.rotate(cpp_arr, k)
        
        nums.clear()
        for i in range(cpp_arr.size()):
            nums.append(cpp_arr[i])