# -------------------------------------------------------------
# PyJdate
# -------------------------------------------------------------
#
#  @ فارسی : توابع زمان و تاریخ هجری شمسی (جلالی) در پایتون
#  @name: Hijri_Shamsi,Solar(Jalali) Date and Time Functions
#  @Author : Reza Gholampanahi & WebSite : http://jdf.scr.ir
#  @License: GNU/LGPL _ Open Source & Free : [all functions]
#  @Ver: 2 | Edited by : Ali Abdollahi  |  www.aabdollahi.ir
#
###############################################################

def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if (gy > 1600):
        jy = 979
        gy -= 1600
    else:
        jy = 0
        gy -= 621
    if (gm > 2):
        gy2 = gy + 1
    else:
        gy2 = gy
    days = (365 * gy) + (int((gy2 + 3) / 4)) - (int((gy2 + 99) / 100)) + (int((gy2 + 399) / 400)) - 80 + gd + g_d_m[
        gm - 1]
    jy += 33 * (int(days / 12053))
    days %= 12053
    jy += 4 * (int(days / 1461))
    days %= 1461
    if (days > 365):
        jy += int((days - 1) / 365)
        days = (days - 1) % 365
    if (days < 186):
        jm = 1 + int(days / 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + int((days - 186) / 30)
        jd = 1 + ((days - 186) % 30)
    return [jy, jm, jd]

def jalali_to_gregorian(jy, jm, jd):
    if (jy > 979):
        gy = 1600
        jy -= 979
    else:
        gy = 621
    if (jm < 7):
        days = (jm - 1) * 31
    else:
        days = ((jm - 7) * 30) + 186
    days += (365 * jy) + ((int(jy / 33)) * 8) + (int(((jy % 33) + 3) / 4)) + 78 + jd
    gy += 400 * (int(days / 146097))
    days %= 146097
    if (days > 36524):
        gy += 100 * (int(--days / 36524))
        days %= 36524
        if (days >= 365):
            days += 1
    gy += 4 * (int(days / 1461))
    days %= 1461
    if (days > 365):
        gy += int((days - 1) / 365)
        days = (days - 1) % 365
    gd = days + 1
    if ((gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0)):
        kab = 29
    else:
        kab = 28
    sal_a = [0, 31, kab, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    gm = 0
    while (gm < 13):
        v = sal_a[gm]
        if (gd <= v):
            break
        gd -= v
        gm += 1
    return [gy, gm, gd]

def tr_num(strx, mod='en', mf='٫'):
    data = strx
    num_a = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
    key_a = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', mf)
    if (mod == 'en'):
        for n, i in enumerate(key_a): data = data.replace(i, num_a[n])
    else:
        for n, i in enumerate(num_a): data = data.replace(i, key_a[n])
    return data

def jcheckdate(jm, jd, jy):
    data = tr_num(str(jm) + '_' + str(jd) + '_' + str(jy))
    jm, jd, jy = data.split('_')

    if (int(jm) == 12):
        if ((((int(jy) % 33) % 4) - 1) == ((int)((int(jy) % 33) * 0.05))):
            l_d = 30
        else:
            l_d = 29
    else:
        l_d = 31 - (int)(int(jm) / 6.5)

    if (int(jm) > 12 or int(jd) > l_d or int(jm) < 1 or int(jd) < 1 or int(jy) < 1):
        return False
    else:
        return True

def jwss(num):
    tmpnum = int(num)
    sl = len(str(num))
    tmp_xy3 = str(tmpnum)[2 - sl:-1]
    xy3 = int(tmp_xy3)
    h3 = h34 = h4 = ''
    if (xy3 == 1):
        p34 = ''
        k34 = ('ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده')
        h34 = k34[num[2 - sl: 2] - 10]
    else:
        xy4 = str(num)[3 - sl:]
        if(xy3 == 0 or xy4 == '0'):
            p34 = ''
        else:
            p34 = ' و '
        k3 = ('', '', 'بیست', 'سی', 'چهل', 'پنجاه', 'شصت', 'هفتاد', 'هشتاد', 'نود')
        h3 = k3[xy3]
        k4 = ('', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه')
        h4 = k4[int(xy4)]
    arss = ""
    if (num > 99):
        tmpsnum = str(num)[0:2]
        if(tmpsnum=='12'):
            arss='هزار و دویست'
        elif(tmpsnum=='13'):
            arss='هزار و سیصد'
        elif(tmpsnum=='14'):
            arss='هزار و چهارصد'
        elif(tmpsnum=='19'):
            arss='هزار و نهصد'
        elif(tmpsnum=='20'):
            arss='دوهزار'

        if (str(num)[2:2] == '00'):
            arss += ''
        else:
            arss += ' و '
    else:
        arss += ''
    ss = arss + h3 + p34 + h34 + h4
    return ss

def jwmm(num):
    key = ('فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند')
    return key[num - 1]

def jwrr(num):
    key = ('یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه', 'ده', 'یازده', 'دوازده', 'سیزده'
           , 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده', 'بیست', 'بیست و یک', 'بیست و دو', 'بیست و سه'
           , 'بیست و چهار', 'بیست و پنج', 'بیست و شش', 'بیست و هفت', 'بیست و هشت', 'بیست و نه', 'سی', 'سی و یک')
    return key[num - 1]

def jwrh(num):
    key = ('شنبه','یکشنبه', 'دوشنبه', 'سه شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه')
    return key[num]

def jwsh(num):
    key = ('مار', 'اسب', 'گوسفند', 'میمون', 'مرغ', 'سگ', 'خوک', 'موش', 'گاو', 'پلنگ', 'خرگوش', 'نهنگ')
    return key[num % 12]

def jwmb(num):
    key = ('حمل', 'ثور', 'جوزا', 'سرطان', 'اسد', 'سنبله', 'میزان', 'عقرب', 'قوس', 'جدی', 'دلو', 'حوت')
    return key[num - 1]

def jwff(num):
    key = ('بهار', 'تابستان', 'پاییز', 'زمستان')
    return key[int((num/3.1))]

def jwkm(num):
    key = ('فر', 'ار', 'خر', 'تی‍', 'مر', 'شه‍', 'مه‍', 'آب‍', 'آذ', 'دی', 'به‍', 'اس‍')
    return key[num - 1]

def jwkh(num):
    key = ('ش','ی', 'د', 'س', 'چ', 'پ', 'ج')
    return key[num-1]

def jdate_words(array, mod=''):
    arrayx = {}
    for num in array:
        tmpnum = int(tr_num(str(num[1])))
        tmpkey = str(num[0])

        if(tmpkey == 'ss'):
            arrayx['ss'] = jwss(tmpnum)
        elif(tmpkey == 'mm'):
            arrayx['mm'] = jwmm(tmpnum)
        elif(tmpkey == 'rr'):
            arrayx['rr'] = jwrr(tmpnum)
        elif(tmpkey == 'rh'):
            arrayx['rh'] = jwrh(tmpnum)
        elif(tmpkey == 'sh'):
            arrayx['sh'] = jwsh(tmpnum)
        elif(tmpkey == 'mb'):
            arrayx['mb'] = jwmb(tmpnum)
        elif(tmpkey == 'ff'):
            arrayx['ff'] = jwff(tmpnum)
        elif(tmpkey == 'km'):
            arrayx['km'] =jwkm(tmpnum)
        elif(tmpkey == 'kh'):
            arrayx['kh'] = jwkh(tmpnum)

    if (mod == ''):
        return arrayx
    else:
        mod.join(arrayx)
