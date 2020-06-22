# 2 7 14 / 5 8 11 /3 5 8 /5 10 11/2 7 11/4 7 9/6 9 11/4 7 13 /2 7 8
# 3 8 13
# 4 11 15
# 6 7 15
# 4 9 13
# 6 11 15
# 6 10 12
# 3 6 11
# 4 9 12
# 4 7 13
# 3 11 15
don = 0
sum = 5000




print('금액이 부족합니다.')
            print('총 금액은' + str(sum) + '원입니다.')
            print('부족한 금액은', str(sum - don1), '입니다.')

            while True:
                don2 = int(input('금액을 넣어주세요 : '))
                don3 = don2 + don1
                if don3 == sum:
                    print('계산이 완료되었습니다. 감사합니다.')
                    break
                elif don3 > sum:
                    print('계산이 완료되었습니다. 잔돈은', str(don1 - sum), '입니다.')
                    print('감사합니다.')
                    break
                while don3 < sum:
                    don2 = int(input('금액을 넣어주세요 : '))
                    don3 = don2 + don1
                    print('부족한 금액', sum - don1, '원을 넣어주세요.')
                    break
            print('결제가 완료되었습니다 감사합니다.')
            break