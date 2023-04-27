import qrcode

def create_image_qr(request):

    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=4,
        )

    qr.add_data(request.POST.get("linkQr"))
    img_qr = qr.make(fit=False)
    img_qr = qr.make_image(fill_color="black", back_color="white")
    img_qr_url = request.POST.get("titleQr")+"abc.png"
    img_qr.save("images/" + img_qr_url)
    return img_qr_url