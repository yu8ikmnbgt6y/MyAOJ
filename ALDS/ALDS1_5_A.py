import sys
import io

input_txt="""
20
1 34 44 63 30 1 9 53 57 57 20 12 52 44 6 9 94 31 67 70
200
1933 918 1848 1973 869 981 224 550 1593 165 170 552 428 191 625 636 921 1945 1311 1863 485 1364 1302 711 1237 1877 432 1930 398 676 492 191 1345 135 426 1630 31 728 1127 1744 1335 105 761 1750 1621 257 933 1573 1614 491 510 1120 1406 1696 50 328 720 1498 825 597 650 1357 185 1094 246 1008 1307 510 755 353 1666 784 739 802 1691 1331 1338 196 657 1964 12 1428 43 1107 969 213 1002 511 481 659 572 1332 815 848 565 1198 1626 439 932 19 488 152 1188 1914 180 996 1751 1751 914 1563 1135 274 1548 522 831 1141 1558 1679 727 504 598 409 894 1989 1239 1086 94 1189 721 1212 747 388 1711 1210 1888 669 1104 1474 1901 1675 1106 184 953 371 1788 1303 1411 1906 111 1401 1997 143 586 1861 1048 1925 1732 1159 1387 1220 401 1416 56 1683 1875 1062 1007 1603 1269 1366 471 519 724 90 1107 320 1131 1656 733 1994 1975 1596 811 1674 1056 731 96 246 706 1695 949 1874 354 475 761 742 757 1645 1144 1641
"""


sys.stdin = io.StringIO(input_txt)
tmp = input()


# copy the below part and paste to the submission form.
# ---------function------------
def main():
    input()
    array_a = list(map(int, input().split()))
    input()
    array_q = map(int, input().split())

    def can_construct_q (q, i, sum_sofar):
        if sum_sofar == q or sum_sofar + array_a[i] == q:
            return True
        elif sum_sofar > q or i >= len(array_a) - 1:
            return False
        if can_construct_q(q, i + 1, sum_sofar + array_a[i]):
            return True
        if can_construct_q(q, i + 1, sum_sofar):
            return True
    sum_array_a = sum(array_a)
    for q in array_q:
        #print(q)
        if sum_array_a < q:
            print('no')
        elif can_construct_q(q, 0, 0):
            print('yes')
        else:
            print('no')
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
