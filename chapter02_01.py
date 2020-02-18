# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 :

# 기본 출력
# 작은따옴표(일반적)
print('Python Start!')
# 큰따옴표
print("Python Start!")
# 작은따옴표 3개
print('''Python Start!''')
# 큰따옴표 3개
print("""Python Start!""")
#줄바꿈
print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='   ')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
# 마지막 부분을 어떻게 처리할 것인지.
# end에 들어간 문자대로 처리, 다음 프린트 문에 이어줄 수 있다.
print('Welcome to', end=' ')
print('IT news', end=' ')
print('Web Site')

# file 옵션
# import 는 예약어
import sys
# sys.stdout 은 콘솔출력
print('Learn Python', file=sys.stdout)
print()

# 이번강의에서 가장 중요
# format 사용(d : 3(정수), s : 'python'(문자열), f : '3.1445454'(실수))
# 정석적
print('%s %s' % ('one', 'two'))
# 포멧함수가 내부적으로 처리해줌
print('{} {}'.format('one', 'two'))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))

print()

# %s
# 오른쪽부터 채우기
# 총 자릿수. 10개 오른쪽부터 채우기
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

# 총 자릿수. 10개 왼쪽부터 채우기
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

# 공백을 밑줄로 채우기
print('{:_>10}'.format('nice'))
# 중앙 정렬
print('{:^10}'.format('nice'))

# 자릿수 5개, 5까지 자르기
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
# 10글자의 자리를 확보하는데, 5개만 나와라
print('{:10.5}'.format('pythonstudy'))
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' %(42))
print('{:4d}'.format(42))
print()
# %f
print('%f' % (3.143434343443))
print('{:f}'.format(3.143434343443))
print()
# 총 6자리, 소수부는 2자리
print('%06.2f' % (3.1415926563689793))
print('{:06.2f}'.format(3.1415926563689793))