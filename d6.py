num = int(input("type : "))
def chan(num):
    ones = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ"]
    tens = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"]
    hundreds = ["", "หนึ่งร้อย", "สองร้อย", "สามร้อย", "สี่ร้อย", "ห้าร้อย", "หกร้อย", "เจ็ดร้อย", "แปดร้อย", "เก้าร้อย"]
    data = ""
    if num >= 100:
        data += hundreds[num//100]
        num % 100
    if num >= 10:
        data += tens[num//10]
    else:
        data += ones[ones//1]
    return (data)
cc = chan(num)
print(cc)