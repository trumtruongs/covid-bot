from django.utils import timezone
import pytz
from countries.models import Country, History
from covidbot import settings
from webhooks import send
from covidbot.commons import flag_url


def statistics_replies(sender_id, page_id):
    countries = (('TE', 'Thế Giới'), ('VN', 'Việt Nam'), ('US', 'Hoa Kỳ'), ('IT', 'Italia'), ('CN', 'Trung Quốc'),)
    quick_replies = [{
        'content_type': 'text',
        'title': country[1],
        'payload': 'STATISTICS {}'.format(country[0]),
        'image_url': flag_url(country[0]) if country[0] is not 'TE' else 'https://www.who.int/images/default-source/default-album/who-emblem-rgb.png'
    } for country in countries]
    quick_replies.append({
        'content_type': 'text',
        'title': 'Khác',
        'payload': 'STATISTICS MORE'
    })
    text = 'ABC'
    send.quick_reply(sender_id, page_id, text, quick_replies)


def detect_quick_reply(sender_id, page_id, payload):
    if payload.startswith('STATISTICS '):
        quick_reply_statistics(sender_id, page_id, payload)


def quick_reply_statistics(sender_id, page_id, payload):
    if payload[-4:] == 'MORE':
        send.text_message(sender_id, page_id,
                          'Để xem thống kê của các nước khác. Hãy gửi tin nhắn với cú pháp: @TK [MÃ QUỐC GIA]\nVí dụ: @TK VN')
    else:
        code = payload[-2:]
        content = '''*{name}*
================
Số ca nhiễm: {cases:,}
Đã bình phục: {recovered:,}
Tử vong: {death:,}

Hôm nay {today}:
================
Số ca nhiễm: {cases_today:,}
Đã bình phục: {recovered_today:,}
Tử vong: {death_today:,}

================
Cập nhật lúc: {updated_at}
                '''
        try:
            country = Country.objects.get(code=code)
            cases_today = death_today = recovered_today = 0
            now = timezone.now()
            try:
                today = History.objects.get(country=country, date__day=now.day, date__month=now.month,
                                            date__year=now.year)
                cases_today = today.cases
                death_today = today.death
                recovered_today = today.recovered
            except History.DoesNotExist:
                pass
            content = content.format(name=country.name,
                                     cases=country.cases,
                                     death=country.death,
                                     recovered=country.recovered,
                                     today=country.updated_at.strftime('%d/%m/%Y'),
                                     cases_today=cases_today,
                                     death_today=death_today,
                                     recovered_today=recovered_today,
                                     updated_at=timezone.localtime(country.updated_at, pytz.timezone(settings.TIME_ZONE)).strftime('%H:%M %d/%m/%Y')
                                     )
            send.text_message(sender_id, page_id, content)

        except Country.DoesNotExist:
            send.text_message(sender_id, page_id, 'Quốc gia có mã {} hiện chưa có dữ liệu!'.format(code))
            send.text_message(sender_id, page_id,
                              """Để xem thống kê của các nước khác. Hãy gửi tin nhắn với cú pháp: @TK [MÃ QUỐC GIA]
Ví dụ: @TK VN""")
