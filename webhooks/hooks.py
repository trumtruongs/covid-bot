from patients.models import Patient
from webhooks import send
from webhooks.quick_replies import quick_reply_statistics


def get_patient(fbid, page_id, patient_index):
    try:
        patient_code = str(patient_index).strip()
        info = Patient.objects.get(code=patient_code)
        response_message = 'Bệnh nhân ' + patient_index + ':'
        if not info.is_healthy:
            if info.gender == 'male':
                response_message += ' Nam,'
            elif info.gender == 'female':
                response_message += ' Nữ,'
            if info.year_of_birth:
                response_message += ' {} tuổi,'.format(2020-info.year_of_birth)
            response_message += ' ' + info.detail
        else:
            response_message += ' đã khỏi bệnh.'
        send.text_message(fbid, page_id, response_message)
    except Patient.DoesNotExist:
        send.text_message(fbid, page_id, "Mã số bệnh nhân không tồn tại!")


def handle_finding(fbid, page_id, message_text):
    signal = message_text[:3]
    if signal.lower() == '@bn':
        get_patient(fbid, page_id, message_text[3:])
    elif signal.lower() == '@tk':
        quick_reply_statistics(fbid, page_id, message_text.upper())
