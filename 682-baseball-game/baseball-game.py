class Solution:
    def calPoints(self, operations: list[str]) -> int:
        st = []
        for i in range(len(operations)):
            ops = operations[i]
            if ops.strip('-').isdigit():
                st.append(int(ops))
            if ops == "+":
                st.append(st[-1] + st[-2])
            if ops == 'D':
                st.append(st[-1]*2)
            if ops == 'C':
                st.pop()
        return sum(st)


        