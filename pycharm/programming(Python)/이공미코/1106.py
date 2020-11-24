def solution(height):
   count = 0
   for i in range(len(height)):
	    for j in range(len(height[i])):
		    if i > 0:
                if not (height[i - 1][j] > height[i][j]):
                    continue
            if j > 0:
                if not (height[i][j - 1] > height[i][j]):
                    continue
            if i < len(height) - 1:
                if not (height[i + 1][j] > height[i][j]:
                    continue
            if j < len (height[i]) - 1:
                if not (height[i][j + 1] > height[i][j]):
                    continue
        count += 1
   return count

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

