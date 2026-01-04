import math 

def main():
    print("PYB101x - Assigment01")
    xA = float(input(" Nhập tộ độ x của điểm A "))
    yA = float(input(" Nhập tộ độ y của điểm A "))
    xB = float(input(" Nhập tộ độ x của điểm B "))
    yB = float(input(" Nhập tộ độ y của điểm B "))
    xC = float(input(" Nhập tộ độ x của điểm C "))
    yC = float(input(" Nhập tộ độ y của điểm C "))
    
    def khoangcach() :
        AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
        BC = math.sqrt((xC - xB)**2 + (yC - yB)**2)
        AC = math.sqrt((xC - xA)**2 + (yC - yA)**2)

        print("Độ dài cạnh AB =", round(AB, 2), "cm")
        print("Độ dài cạnh BC =", round(BC, 2), "cm")
        print("Độ dài cạnh AC =", round(AC, 2), "cm")
        return AB, BC, AC 

    def kiemtra_tamgiac(AB, BC, AC) :
        if BC + AC > AB and AC + AB > BC and AB + BC > AC :
            print("A,B, C là một tam giác")
        else :
            print("A,B, C không phải là một tam giác")

    def goc(AB, BC, AC) : 

        cosA = (AB**2 + AC**2 - BC**2) / (2 * AB * AC)
        cosB = (AB**2 + BC**2 - AC**2) / (2 * AB * BC)
        cosC = (AC**2 + BC**2 - AB**2) / (2 * AC * BC)

        cosA = max(-1, min(1, cosA))
        cosB = max(-1, min(1, cosB))
        cosC = max(-1, min(1, cosC))

        A = math.degrees(math.acos(cosA))
        B = math.degrees(math.acos(cosB))
        C = math.degrees(math.acos(cosC))

        print("Góc BAC =", round(A, 2), "(độ)")
        print("Góc ABC =", round(B, 2), "(độ)")
        print("Góc BCA =", round(C, 2), "(độ)")
        return A, B, C
    
    def loai_tamgiac(AB, BC, AC, A, B, C) :
        # TAM GIÁC VUÔNG
        if A == 90 and AB != AC : 
            loai = "Tam giác vuông tại đỉnh A"
        elif B == 90 and AB != BC :
            loai = "Tam giác vuông tại đỉnh B"
        elif C == 90 and BC != AC :
            loai = "Tam giác vuông tại đỉnh C"
        # TAM GIÁC TÙ 
        elif A > 90 and AB != AC :
            loai = "Tam giác tù tại góc A"
        elif B > 90 and AB != BC :
            loai = "Tam giác tù tại góc B"
        elif C > 90 and BC != AC :
            loai = "Tam giác tù tại góc C"
        # TAM GIÁC TÙ VÀ CÂN 
        elif A > 90 and AB == AC :
            loai = "Tam giác tù và cân tại góc A"
        elif B > 90 and AB == BC :
            loai = "Tam giác tù và cân tại góc B"
        elif C > 90 and BC == AC :
            loai = "Tam giác tù và cân tại góc C"
        # TAM GIÁC CÂN
        elif AB == AC and A != 90 :
            loai = "Tam giác cân tại đỉnh A"
        elif AB == BC and B != 90 :
            loai = "Tam giác cân tại đỉnh B"
        elif AC == BC and C != 90 :
            loai = "Tam giác cân tại đỉnh C"
        # TAM GIÁC VUÔNG CÂN
        elif AB == AC and A == 90 :
            loai =  "Tam giác vuông cân tại đỉnh A"
        elif AB == BC and B == 90 :
            loai =  "Tam giác vuông cân tại đỉnh B"
        elif AC == BC and C == 90 :
            loai =  "Tam giác vuông cân tại đỉnh C"
        # TAM GIÁC ĐỀU 
        elif AB == BC == AC :
            loai =  "Tam giác đều"
        else :
            loai = "Tam giác thường"
        return loai  
    
    def dientich_tamgiac() :
        S = 0.5 * (xA*(yB - yC) + xB*(yC - yA) + xC*(yA - yB))
        S = abs(S)
        print("Diện tích của tam giác =", round(S, 2))
        return S 

    def duongcao_tamgiac(AB, BC, AC, S) :
        hA = 2*S/BC 
        hB = 2*S/AC
        hC = 2*S/AB

        print("Độ dài đường cao từ điểm A =", round(hA, 2))
        print("Độ dài đường cao từ điểm B =", round(hB, 2))
        print("Độ dài đường cao từ điểm C =", round(hC, 2))
        return hA, hB, hC 
    
    def trungtuyen_tamgiac(AB, BC, AC) :
        mA = 0.5 * math.sqrt(2*AB**2 + 2*AC**2 - BC**2) 
        mB = 0.5 * math.sqrt(2*AB**2 + 2*BC**2 - AC**2) 
        mC = 0.5 * math.sqrt(2*BC**2 + 2*AC**2 - AB**2) 

        print("Độ dài trung tuyến từ điểm A =", round(mA, 2))
        print("Độ dài trung tuyến từ điểm B =", round(mB, 2))
        print("Độ dài trung tuyến từ điểm C =", round(mC, 2))
        return mA, mB, mC 
    
    def trongtam_tamgiac() :
        xG = (xA + xB + xC) / 3
        yG = (yA + yB + yC) / 3
        print("Tọa độ trọng tâm của tam giác ABC:", f"x = {xG} ; y = {yG}")
        return f"x = {xG} ; y = {yG}"
    
    def tructam_tamgiac(AB, BC, AC, S) : 
        xH = (BC**2 * (yB - yC) + AC**2 * (yC - yA) + AB**2 * (yA - yB)) / (4 * S)
        yH = (BC**2 * (xC - xB) + AC**2 * (xA - xC) + AB**2 * (xB - xA)) / (4 * S)
        print("Tọa độ trực tâm của tam giác ABC:", f"x = {xH} ; y = {yH}")
        return xH, yH

    AB, BC, AC = khoangcach()
    kiemtra_tamgiac(AB, BC, AC)  
    A, B, C = goc(AB, BC, AC)
    loai = loai_tamgiac(AB, BC, AC, A, B, C)  
    print("Loại của tam giác ABC:", loai)
    S = dientich_tamgiac()
    duongcao_tamgiac(AB, BC, AC, S)
    trungtuyen_tamgiac(AB, BC, AC) 
    trongtam_tamgiac()
    tructam_tamgiac(AB, BC, AC, S)

if __name__ == '__main__':
    main()


    