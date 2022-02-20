class Solution:
    def simplifyPath(self, path: str) -> str:
        
        new_path = path.replace("//", "/")
        
        while new_path != path:
            path = new_path
            new_path = path.replace("//", "/")
            
        new_path_lst = new_path.split("/")
        print(new_path_lst)
        
        stack = []
        for i in new_path_lst:
            if i == '' or i == '.':
                pass
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
                    
        result = ""
        for j in stack:
            result += "/"
            result += j
        
        if result == '':
            return "/"
        
        return result