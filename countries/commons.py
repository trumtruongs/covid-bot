import requests
import json
from countries.models import Country, History
import pycountry
import flag
import _thread
from webhooks import send


def fetch_new_statistics():
    res = requests.get('https://ncovi.vnpt.vn/thongtindichbenh_v2')
    content = res.content
    try:
        data = json.loads(content)['data']
        for c in data['TG']:
            try:
                province_name = c['province_name']
                cases = c['confirmed']
                death = c['deaths']
                recovered = c['recovered']

                cases_today = c['increase_confirmed']
                death_today = c['increase_deaths']
                recovered_today = c['increase_recovered']

                if province_name == 'Thế giới':
                    code = 'TE'
                    name = 'Thế Giới'
                else:
                    search = pycountry.countries.search_fuzzy(province_name)
                    if len(search) == 0:
                        raise Exception('')
                    code = search[0].alpha_2
                    name = '{} {}'.format(province_name, flag.flag(code))

                if province_name == 'Vietnam':
                    name = 'Việt Nam {}'.format(flag.flag('VN'))
                elif province_name == 'USA':
                    name = 'Mỹ {}'.format(flag.flag('US'))
                elif province_name == 'China':
                    name = 'Trung Quốc {}'.format(flag.flag('CN'))
                elif province_name == 'Russia':
                    name = 'Nga {}'.format(flag.flag('RU'))
                elif province_name == 'Japan':
                    name = 'Nhật Bản {}'.format(flag.flag('JP'))

                print(code)
                country, created = Country.objects.update_or_create(
                    code=code,
                    defaults={'name': name, 'cases': cases, 'death': death, 'recovered': recovered}
                )
                # Check Vietnam increase
                defaults = {'cases': cases_today, 'death': death_today, 'recovered': recovered_today}
                history, created = History.objects.get_or_create(country=country, defaults=defaults)
                old = {'cases': history.cases, 'death': history.death, 'recovered': history.recovered}
                if not created:
                    history.cases = cases_today
                    history.death = death_today
                    history.recovered = recovered_today
                    history.save()
                if code == 'VN':
                    if old['cases'] != defaults['cases'] or old['death'] != defaults['death'] or old['recovered'] != defaults['recovered']:
                        _thread.start_new_thread(send.notify_admin, (old, defaults))

            except (LookupError, Exception):
                pass
    except ValueError:
        pass
