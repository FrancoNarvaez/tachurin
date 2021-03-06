from turtle import ycor
from re import A, L
from unicodedata import decimal
import unittest


def test_convert_roman_to_decimal(decimal):

    def invertir_cadena_manual(numero):
        cadena_invertida = ""
        for letra in numero:
            cadena_invertida = letra + cadena_invertida
        return cadena_invertida
    
    romano = list(invertir_cadena_manual(decimal))
    romano.reverse()
    
    def conversion_romano_to_numero():
        for x in romano: 
            letra_1 = int
            letra_2 = int
            letra_3 = int
            letra_4 = int
            letra_5 = int
            if (x) == "I":
                letra_1 = 1 + letra_1
            elif (x) == "V":
                letra_2 = 5
            elif (x) == "X":
                letra_3 = 10 + letra_3
            elif (x) == "L":
                letra_4 = 50
            elif (x) == "C":
                letra_5 = 100
        return list(letra_1,letra_2,letra_3,letra_4,letra_5)

    tremenda_lista = conversion_romano_to_numero()
    
    for i in range(5):
        a = int
        b = int
        if  tremenda_lista(i) >= tremenda_lista(i + 1):
            b = tremenda_lista(i + 1) - tremenda_lista(i)
        if tremenda_lista(i) < tremenda_lista(i + 1):
            b = tremenda_lista(i + 1) + tremenda_lista(i)
        a = a + b
        return a
        


class TestRomanToNumber(unittest.TestCase):
    def test_1(self):
        roman_number = test_convert_roman_to_decimal("I")
        self.assertEqual(roman_number,1)
    def test_2(self):
        roman_number = test_convert_roman_to_decimal("II")
        self.assertEqual(roman_number,2)
    def test_3(self):
        roman_number = test_convert_roman_to_decimal("III")
        self.assertEqual(roman_number,3)
    def test_4(self):
        roman_number = test_convert_roman_to_decimal("IV")
        self.assertEqual(roman_number,4)
    def test_5(self):
        roman_number = test_convert_roman_to_decimal("V")
        self.assertEqual(roman_number,5)
    def test_6(self):
        roman_number = test_convert_roman_to_decimal("VI")
        self.assertEqual(roman_number,6)
    def test_7(self):
        roman_number = test_convert_roman_to_decimal("VII")
        self.assertEqual(roman_number,7)
    def test_8(self):
        roman_number = test_convert_roman_to_decimal("VIII")
        self.assertEqual(roman_number,8)
    def test_9(self):
        roman_number = test_convert_roman_to_decimal("IX")
        self.assertEqual(roman_number,9)
    def test_10(self):
        roman_number = test_convert_roman_to_decimal("X")
        self.assertEqual(roman_number,10)
    def test_11(self):
        roman_number = test_convert_roman_to_decimal("XI")
        self.assertEqual(roman_number,11)
    def test_12(self):
        roman_number = test_convert_roman_to_decimal("XII")
        self.assertEqual(roman_number,12)
    def test_13(self):
        roman_number = test_convert_roman_to_decimal("XIII")
        self.assertEqual(roman_number,13)
    def test_14(self):
        roman_number = test_convert_roman_to_decimal("XIV")
        self.assertEqual(roman_number,14)
    def test_15(self):
        roman_number = test_convert_roman_to_decimal("XV")
        self.assertEqual(roman_number,15)
    def test_16(self):
        roman_number = test_convert_roman_to_decimal("XVI")
        self.assertEqual(roman_number,16)
    def test_17(self):
        roman_number = test_convert_roman_to_decimal("XVII")
        self.assertEqual(roman_number,17)
    def test_18(self):
        roman_number = test_convert_roman_to_decimal("XVIII")
        self.assertEqual(roman_number,18)
    def test_19(self):
        roman_number = test_convert_roman_to_decimal("XIX")
        self.assertEqual(roman_number,19)
    def test_20(self):
        roman_number = test_convert_roman_to_decimal("XX")
        self.assertEqual(roman_number,20)
    def test_21(self):
        roman_number = test_convert_roman_to_decimal("XXI")
        self.assertEqual(roman_number,21)
    def test_22(self):
        roman_number = test_convert_roman_to_decimal("XXII")
        self.assertEqual(roman_number,22)
    def test_23(self):
        roman_number = test_convert_roman_to_decimal("XXIII")
        self.assertEqual(roman_number,23)
    def test_24(self):
        roman_number = test_convert_roman_to_decimal("XXIV")
        self.assertEqual(roman_number,24)
    def test_25(self):
        roman_number = test_convert_roman_to_decimal("XXV")
        self.assertEqual(roman_number,25)
    def test_26(self):
        roman_number = test_convert_roman_to_decimal("XXVI")
        self.assertEqual(roman_number,26)
    def test_27(self):
        roman_number = test_convert_roman_to_decimal("XXVII")
        self.assertEqual(roman_number,27)
    def test_28(self):
        roman_number = test_convert_roman_to_decimal("XXVIII")
        self.assertEqual(roman_number,28)
    def test_29(self):
        roman_number = test_convert_roman_to_decimal("XXIX")
        self.assertEqual(roman_number,29)
    def test_30(self):
        roman_number = test_convert_roman_to_decimal("XXX")
        self.assertEqual(roman_number,30)
    def test_31(self):
        roman_number = test_convert_roman_to_decimal("XXXI")
        self.assertEqual(roman_number,31)
    def test_32(self):
        roman_number = test_convert_roman_to_decimal("XXXII")
        self.assertEqual(roman_number,32)
    def test_33(self):
        roman_number = test_convert_roman_to_decimal("XXXIII")
        self.assertEqual(roman_number,33)
    def test_34(self):
        roman_number = test_convert_roman_to_decimal("XXXIV")
        self.assertEqual(roman_number,34)
    def test_35(self):
        roman_number = test_convert_roman_to_decimal("XXXV")
        self.assertEqual(roman_number,35)
    def test_36(self):
        roman_number = test_convert_roman_to_decimal("XXXVI")
        self.assertEqual(roman_number,36)
    def test_37(self):
        roman_number = test_convert_roman_to_decimal("XXXVII")
        self.assertEqual(roman_number,37)
    def test_38(self):
        roman_number = test_convert_roman_to_decimal("XXXVIII")
        self.assertEqual(roman_number,38)
    def test_39(self):
        roman_number = test_convert_roman_to_decimal("XXXIX")
        self.assertEqual(roman_number,39)
    def test_40(self):
        roman_number = test_convert_roman_to_decimal("XL")
        self.assertEqual(roman_number,40)
    def test_41(self):
        roman_number = test_convert_roman_to_decimal("XLI")
        self.assertEqual(roman_number,41)
    def test_42(self):
        roman_number = test_convert_roman_to_decimal("XLII")
        self.assertEqual(roman_number,42)
    def test_43(self):
        roman_number = test_convert_roman_to_decimal("XLIII")
        self.assertEqual(roman_number,43)
    def test_44(self):
        roman_number = test_convert_roman_to_decimal("XLIV")
        self.assertEqual(roman_number,44)
    def test_45(self):
        roman_number = test_convert_roman_to_decimal("XLV")
        self.assertEqual(roman_number,45)
    def test_46(self):
        roman_number = test_convert_roman_to_decimal("XLVI")
        self.assertEqual(roman_number,46)
    def test_47(self):
        roman_number = test_convert_roman_to_decimal("XLVII")
        self.assertEqual(roman_number,47)
    def test_48(self):
        roman_number = test_convert_roman_to_decimal("XLVIII")
        self.assertEqual(roman_number,48)
    def test_49(self):
        roman_number = test_convert_roman_to_decimal("XLIX")
        self.assertEqual(roman_number,49)
    def test_50(self):
        roman_number = test_convert_roman_to_decimal("L")
        self.assertEqual(roman_number,50)
    def test_51(self):
        roman_number = test_convert_roman_to_decimal("LI")
        self.assertEqual(roman_number,51)
    def test_52(self):
        roman_number = test_convert_roman_to_decimal("LII")
        self.assertEqual(roman_number,52)
    def test_53(self):
        roman_number = test_convert_roman_to_decimal("LIII")
        self.assertEqual(roman_number,53)
    def test_54(self):
        roman_number = test_convert_roman_to_decimal("LIV")
        self.assertEqual(roman_number,54)
    def test_55(self):
        roman_number = test_convert_roman_to_decimal("LV")
        self.assertEqual(roman_number,55)
    def test_56(self):
        roman_number = test_convert_roman_to_decimal("LVI")
        self.assertEqual(roman_number,56)
    def test_57(self):
        roman_number = test_convert_roman_to_decimal("LVII")
        self.assertEqual(roman_number,57)
    def test_58(self):
        roman_number = test_convert_roman_to_decimal("LVIII")
        self.assertEqual(roman_number,58)
    def test_59(self):
        roman_number = test_convert_roman_to_decimal("LIX")
        self.assertEqual(roman_number,59)
    def test_60(self):
        roman_number = test_convert_roman_to_decimal("LX")
        self.assertEqual(roman_number,60)
    def test_61(self):
        roman_number = test_convert_roman_to_decimal("LXI")
        self.assertEqual(roman_number,61)
    def test_62(self):
        roman_number = test_convert_roman_to_decimal("LXII")
        self.assertEqual(roman_number,62)
    def test_63(self):
        roman_number = test_convert_roman_to_decimal("LXIII")
        self.assertEqual(roman_number,63)
    def test_64(self):
        roman_number = test_convert_roman_to_decimal("LXIV")
        self.assertEqual(roman_number,64)
    def test_65(self):
        roman_number = test_convert_roman_to_decimal("LXV")
        self.assertEqual(roman_number,65)
    def test_66(self):
        roman_number = test_convert_roman_to_decimal("LXVI")
        self.assertEqual(roman_number,66)
    def test_67(self):
        roman_number = test_convert_roman_to_decimal("LXVII")
        self.assertEqual(roman_number,67)
    def test_68(self):
        roman_number = test_convert_roman_to_decimal("LXVIII")
        self.assertEqual(roman_number,68)
    def test_69(self):
        roman_number = test_convert_roman_to_decimal("LXIX")
        self.assertEqual(roman_number,69)
    def test_70(self):
        roman_number = test_convert_roman_to_decimal("LXX")
        self.assertEqual(roman_number,70)
    def test_71(self):
        roman_number = test_convert_roman_to_decimal("LXXI")
        self.assertEqual(roman_number,71)
    def test_72(self):
        roman_number = test_convert_roman_to_decimal("LXXII")
        self.assertEqual(roman_number,72)
    def test_13(self):
        roman_number = test_convert_roman_to_decimal("XIII")
        self.assertEqual(roman_number,73)
    def test_74(self):
        roman_number = test_convert_roman_to_decimal("LXXIV")
        self.assertEqual(roman_number,74)
    def test_75(self):
        roman_number = test_convert_roman_to_decimal("LXXV")
        self.assertEqual(roman_number,75)
    def test_76(self):
        roman_number = test_convert_roman_to_decimal("LXXVI")
        self.assertEqual(roman_number,76)
    def test_77(self):
        roman_number = test_convert_roman_to_decimal("LXXVII")
        self.assertEqual(roman_number,77)
    def test_78(self):
        roman_number = test_convert_roman_to_decimal("LXXVIII")
        self.assertEqual(roman_number,78)
    def test_79(self):
        roman_number = test_convert_roman_to_decimal("LXXIX")
        self.assertEqual(roman_number,79)
    def test_80(self):
        roman_number = test_convert_roman_to_decimal("LXXX")
        self.assertEqual(roman_number,80)
    def test_81(self):
        roman_number = test_convert_roman_to_decimal("LXXXI")
        self.assertEqual(roman_number,81)
    def test_82(self):
        roman_number = test_convert_roman_to_decimal("LXXXII")
        self.assertEqual(roman_number,82)
    def test_83(self):
        roman_number = test_convert_roman_to_decimal("LXXXIII")
        self.assertEqual(roman_number,83)
    def test_84(self):
        roman_number = test_convert_roman_to_decimal("LXXXIV")
        self.assertEqual(roman_number,84)
    def test_85(self):
        roman_number = test_convert_roman_to_decimal("LXXXV")
        self.assertEqual(roman_number,85)
    def test_86(self):
        roman_number = test_convert_roman_to_decimal("LXXXVI")
        self.assertEqual(roman_number,86)
    def test_87(self):
        roman_number = test_convert_roman_to_decimal("LXXXVII")
        self.assertEqual(roman_number,87)
    def test_88(self):
        roman_number = test_convert_roman_to_decimal("LXXXVIII")
        self.assertEqual(roman_number,88)
    def test_89(self):
        roman_number = test_convert_roman_to_decimal("LXXXIX")
        self.assertEqual(roman_number,89)
    def test_90(self):
        roman_number = test_convert_roman_to_decimal("XC")
        self.assertEqual(roman_number,90)
    def test_91(self):
        roman_number = test_convert_roman_to_decimal("XCI")
        self.assertEqual(roman_number,91)
    def test_92(self):
        roman_number = test_convert_roman_to_decimal("XCII")
        self.assertEqual(roman_number,92)
    def test_93(self):
        roman_number = test_convert_roman_to_decimal("XCIII")
        self.assertEqual(roman_number,93)
    def test_94(self):
        roman_number = test_convert_roman_to_decimal("XCIV")
        self.assertEqual(roman_number,94)
    def test_95(self):
        roman_number = test_convert_roman_to_decimal("XCV")
        self.assertEqual(roman_number,95)
    def test_96(self):
        roman_number = test_convert_roman_to_decimal("XCVI")
        self.assertEqual(roman_number,96)
    def test_97(self):
        roman_number = test_convert_roman_to_decimal("XCVII")
        self.assertEqual(roman_number,97)
    def test_98(self):
        roman_number = test_convert_roman_to_decimal("XCVIII")
        self.assertEqual(roman_number,98)
    def test_99(self):
        roman_number = test_convert_roman_to_decimal("XCIX")
        self.assertEqual(roman_number,99)
    def test_100(self):
            roman_number = test_convert_roman_to_decimal("C")
            self.assertEqual(roman_number,100)
if __name__=='__main__':
    unittest.main()