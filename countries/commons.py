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
                search = pycountry.countries.search_fuzzy(c['province_name'])
                if len(search) == 0:
                    raise Exception('')
                code = search[0].alpha_2
                name = '{} {}'.format(c['province_name'], flag.flag(code))
                cases = c['confirmed']
                death = c['deaths']
                recovered = c['recovered']

                cases_today = c['increase_confirmed']
                death_today = c['increase_deaths']
                recovered_today = c['increase_recovered']

                if c['province_name'] == 'Thế giới':
                    code = 'TE'
                    name = 'Thế Giới'
                elif c['province_name'] == 'Vietnam':
                    name = 'Việt Nam {}'.format(flag.flag('VN'))
                elif c['province_name'] == 'USA':
                    name = 'Mỹ {}'.format(flag.flag('US'))
                elif c['province_name'] == 'China':
                    name = 'Trung Quốc {}'.format(flag.flag('CN'))
                elif c['province_name'] == 'Russia':
                    name = 'Nga {}'.format(flag.flag('RU'))
                elif c['province_name'] == 'Japan':
                    name = 'Nhật Bản {}'.format(flag.flag('JP'))

                country, created = Country.objects.update_or_create(
                    code=code,
                    defaults={'name': name, 'cases': cases, 'death': death, 'recovered': recovered}
                )
                # Check Vietnam increase
                if code == 'VN':
                    defaults = {'cases': cases, 'death': death, 'recovered': recovered}
                    vn, created = History.objects.get_or_create(country=country, defaults=defaults)
                    if vn.cases != cases or vn.death != death or vn.recovered != recovered:
                        old = {'cases': vn.cases, 'death': vn.death, 'recovered': vn.recovered}
                        _thread.start_new_thread(send.notify_admin, (old, defaults))
                        vn.cases = cases
                        vn.death = death
                        vn.recovered = recovered
                        vn.save()
            except (LookupError, Exception):
                pass
    except ValueError:
        pass
