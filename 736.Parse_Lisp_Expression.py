#coding=utf8
import re

class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        #找到最里层括号里的表达式
        print("process_string  %s" % expression)
        v_map = {}
        value = None
        while " " in expression:
            left = len(expression) - expression[::-1].find('(') - 1
            right = expression.find(")")
            sub_str = expression[left + 1: right]

            #处理该表达式
            v_map, value = self.process_bracket(sub_str, v_map, value)

            expression = expression[:left] + expression[right + 1:]

        return value

    def process_let(self, arr, v_map, value):
        index = 1
        n_map = {}
        while index < len(arr) - 1:
            name = arr[index]
            try:
                n_map[name] = int(arr[index + 1])
            except:
                pass
            index += 2

        if len(arr) % 2 != 0:
            if value is not None:
                return ({}, value)
            else:
                #解出v_map
                x = 0
                y = 0
                try:
                    x = int(v_map[1])
                except ValueError:
                    x = n_map[v_map[1]]

                try:
                    y = int(v_map[2])
                except ValueError:
                    y = n_map[v_map[2]]

                if v_map["type"] == "add":
                    value = x + y
                else:
                    value = x * y
                return({}, value)

        else:
            return({}, n_map[arr[-1]])

    def process_basic(self, arr, v_map, value):
        done = True
        ret_map = {}
        ret_value = None

        try:
            ret_map[1] = int(arr[1])
        except ValueError:
            ret_map[1] = arr[1]
            done = False

        if len(arr) == 3:
            try:
                ret_map[2] = int(arr[2])
            except ValueError:
                ret_map[2] = arr[2]
                done = False
        else:
            ret_map[2] = value

        ret_map["type"] = arr[0]
        if done:
            if arr[0] == "add":
                ret_value = ret_map[1] + ret_map[2]
            elif arr[0] == "mult":
                ret_value = ret_map[1] * ret_map[2]
            else:
                raise Exception("error type: %s" % arr[0])

        return (ret_map, ret_value)

    def process_bracket(self, expression, v_map, value):
        expression = expression.strip()
        print("process_bracket [%s], value: %s, v_map: %s" % (expression, value, v_map))
        arr = re.split('\s+', expression)
        if arr[0] == "let":
            return self.process_let(arr, v_map, value)
        else:
            return self.process_basic(arr, v_map, value)


solution = Solution()
string = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
#string = "(let x 3 x 2 x)"
#string = "(let x 2 (add (let x 3 (let x 4 x)) x))"
string = "(let a1 3 b2 (add a1 1) b2) "
print(solution.evaluate(string))
