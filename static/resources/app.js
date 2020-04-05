(async function genNetworkChart() {
  window.mobilecheck = function () {
    var check = false;
    (function (a) {
      if (
        /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(
          a
        ) ||
        /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(
          a.substr(0, 4)
        )
      )
        check = true;
    })(navigator.userAgent || navigator.vendor || window.opera);
    return check;
  };

  if (window.mobilecheck()) {
    document.querySelector("body").classList.add("mobile");
  }

  am4core.useTheme(am4themes_animated);

  var chart = am4core.create(
    "chartNetwork",
    am4plugins_forceDirected.ForceDirectedTree
  );

  var networkSeries = chart.series.push(
    new am4plugins_forceDirected.ForceDirectedSeries()
  );
  networkSeries.dataFields.value = "value";
  networkSeries.dataFields.linkWith = "linkWith";
  networkSeries.dataFields.name = "name";
  networkSeries.dataFields.children = "children";
  networkSeries.dataFields.color = "color";
  networkSeries.dataFields.age = "Tuổi";
  networkSeries.dataFields.national = "Quốc Tịch";
  networkSeries.dataFields.sex = "Giới Tính";
  networkSeries.dataFields.datein = "Ngày Nhập";
  networkSeries.dataFields.dateout = "Ngày Xuất";
  networkSeries.dataFields.tinh = "Tỉnh";
  networkSeries.dataFields.cachlay = "Cách Lây";
  networkSeries.dataFields.code = "code";
  networkSeries.dataFields.icon = "icon";
  networkSeries.dataFields.diem = "Điểm";
  networkSeries.dataFields.maudiem = "maudiem";
  networkSeries.tooltip.getFillFromObject = false;
  networkSeries.tooltip.background.fill = am4core.color("#4e73df");

  networkSeries.nodes.template.adapter.add("tooltipHTML", function (
    text,
    target
  ) {
    if (target.dataItem) {
      switch (target.dataItem.level) {
        case 0:
          return "<span style='font-size:15px'>Về từ {name}</span>";

        default:
          return `
              <div
                style="
                  display: flex;
                  flex-direction: row;
                  justify-content: center;
                  align-items: center;
                  font-size: 15px;
                "
              >
                <img src="{icon}" alt="Smiley face" height="62" width="62" />
                <table style="margin-left: 20px;">
                  <tr>
                    <th align="left" style="padding: 0 8px 2px 0;">Tuổi</th>
                    <td>{age}</td>
                  </tr>
                  <tr>
                    <th align="left" style="padding: 0 8px 2px 0;">Quốc tịch</th>
                    <td>{national}</td>
                  </tr>
                  <tr>
                    <th align="left" style="padding: 0 8px 2px 0;">Tỉnh</th>
                    <td>{tinh}</td>
                  </tr>
                  <tr></tr>

                  <tr>
                    <th align="left" style="padding: 0 8px 2px 0;">Ngày Nhập Viện</th>
                    <td>{datein}</td>
                  </tr>
                  <tr>
                    <th align="left" style="padding: 0 8px 2px 0;">Ngày Xét Nghiệm</th>
                    <td>{dateout}</td>
                  </tr>
                </table>
              </div>
              <hr style="margin-top: 0.6em; margin-bottom: 0.6em;" />
              <div style="display: flex; justify-content: center; font-size: 12px;">
                {cachlay}
              </div>
            `;
      }
    }
    return text;
  });

  networkSeries.manyBodyStrength = -20;
  networkSeries.links.template.strength = 0.4;

  networkSeries.minRadius = am4core.percent(2);
  networkSeries.centerStrength = 2;
  networkSeries.links.template.strokeWidth = 2;
  networkSeries.nodes.template.label.adapter.add(
    "text",
    (label, target, key) => {
      if (target.dataItem && target.dataItem.level != 0) {
        return "\n\n{name}";
      } else {
        return "[font-size: 12px]{name}[/]";
      }
    }
  );
  networkSeries.nodes.template.label.adapter.add(
    "valign",
    (label, target, key) => {
      if (target.dataItem && target.dataItem.level != 0) {
        return "bottom";
      }
    }
  );
  networkSeries.nodes.template.label.adapter.add(
    "fill",
    (label, target, key) => {
      if (target.dataItem && target.dataItem.level != 0) {
        return am4core.color("#000");
      } else {
        return am4core.color("#fff");
      }
    }
  );
  networkSeries.fontSize = 8;
  networkSeries.maxRadius = 30;
  networkSeries.minRadius = 20;
  networkSeries.nodes.template.adapter.add("fill", function (
    fill,
    target
  ) {
    return fill.lighten(target.dataItem.level * 0.01);
  });

  var icon = networkSeries.nodes.template.createChild(am4core.Image);
  icon.propertyFields.href = "image";
  icon.horizontalCenter = "middle";
  icon.verticalCenter = "middle";
  icon.width = 20;
  icon.height = 20;

  var circleBullet = networkSeries.nodes.template.createChild(
    am4charts.CircleBullet
  );
  circleBullet.dx = 17;
  circleBullet.dy = -26;
  circleBullet.circle.stroke = am4core.color("#fff");

  circleBullet.circle.adapter.add("radius", function (fill, target) {
    if (!target.dataItem.diem || target.dataItem.diem == 0) {
      return 0;
    } else {
      return 8;
    }
  });
  circleBullet.circle.adapter.add("fill", function (fill, target) {
    if (target.dataItem.maudiem) {
      var values = target.dataItem.maudiem;
      return am4core.color(values);
    }
  });
  var icon2 = networkSeries.nodes.template.createChild(
    am4charts.LabelBullet
  );

  icon2.label.adapter.add("text", function (center, target) {
    var values = target.dataItem.diem;
    return values != "0" ? "{diem}" : "";
  });
  icon2.label.fill = am4core.color("#fff");
  icon2.dx = 17;
  icon2.dy = -26;
  icon2.label.fontSize = 8;

  function find(source, id) {
    for (key in source) {
      var item = source[key];
      if (item.name == id) return item;

      if (item.children) {
        var subresult = find(item.children, id);
        if (subresult) return subresult;
      }
    }
    return null;
  }

  function addToData(source, id) {
    for (key in source) {
      var item = source[key];

      if (item.children) {
        var subresult = find(item.children, id[1]);
        if (subresult)
          if (subresult.hasOwnProperty("children")) {
            subresult["children"].push({ name: id[2] });
            return source;
          } else {
            subresult["children"] = [{ name: id[2] }];
            return source;
          }
      }
    }
    return null;
  }

  function addInfoToData(source, id, info) {
    for (key in source) {
      var item = source[key];

      if (item.children) {
        var subresult = find(item.children, id);
        if (subresult) {
          subresult["Tuổi"] = info["Tuổi"] ? info["Tuổi"] : "";
          subresult["Quốc Tịch"] = info["Quốc Tịch"]
            ? info["Quốc Tịch"]
            : "";
          subresult["Tỉnh"] = info["Tỉnh"] ? info["Tỉnh"] : "";
          subresult["Giới Tính"] = info["Giới Tính"]
            ? info["Giới Tính"]
            : "";
          subresult["Ngày Nhập"] = info["Ngày Nhập"]
            ? info["Ngày Nhập"]
            : "";
          subresult["Ngày Xuất"] = info["Ngày Xuất"]
            ? info["Ngày Xuất"]
            : "";
          subresult["Cách Lây"] = info["Cách Lây"]
            ? info["Cách Lây"]
            : "";
          subresult["Điểm"] = info["Điểm"] ? info["Điểm"] : "";
          subresult["maudiem"] = info["maudiem"] ? info["maudiem"] : "";
          subresult["image"] =
            "https://static-ncovi.vnpt.vn/ncovi/ncovi_network/v3/static/flags/" +
            info["code"] +
            ".svg";
          subresult["icon"] =
            "https://static-ncovi.vnpt.vn/ncovi/ncovi_network/v3/static/" +
            info["icon"];
          return source;
        }
      }
    }
    return source;
  }

  function addDepthColor(arr, depth = 0) {
    arr.forEach((obj) => {
      obj.color = listColor[depth];
      obj.level = depth;
      if (obj.hasOwnProperty("children"))
        addDepthColor(obj.children, depth + 1);
    });
  }

  var listColor = [
    "#A8B3BF",
    "#FF5B5D",
    "#AC64F4",
    "#F4A764",
    "#7FFFD4",
    "#159957",
    "#ff9966",
  ];
  var testdata =
    "Trung Quốc--BN001,-BN001-BN002,-BN001-BN003,Trung Quốc--BN004,Trung Quốc--BN005,Trung Quốc--BN006,Trung Quốc--BN007,Trung Quốc--BN008,Trung Quốc--BN009,-BN006-BN010,-BN006-BN011,-BN006-BN012,-BN006-BN013,Trung Quốc--BN014,-BN010-BN015,-BN006-BN016,Anh--BN017,Hàn Quốc--BN018,-BN017-BN019,-BN017-BN020,Anh--BN021,Anh--BN022,Anh--BN023,Anh--BN024,Anh--BN025,Anh--BN026,Anh--BN027,Anh--BN028,Anh--BN029,Anh--BN030,Anh--BN031,Anh--BN032,Anh--BN033,Mỹ--BN034,-BN029-BN035,-BN034-BN036,-BN034-BN037,-BN034-BN038,-BN034-BN039,-BN034-BN040,-BN034-BN041,-BN034-BN042,-BN034-BN043,-BN038-BN044,-BN034-BN045,Anh--BN046,-BN017-BN047,-BN045-BN048,-BN030-BN049,Anh--BN050,Pháp--BN051,Qatar--BN052,Qatar--BN053,Tây Ban Nha--BN054,Anh--BN055,Pháp--BN056,Anh--BN057,Pháp--BN058,Anh--BN059,Pháp--BN060,Malaysia--BN061,Anh--BN062,Anh--BN063,Thụy Sĩ--BN064,-BN045-BN065,Mỹ--BN066,Malaysia--BN067,Singapore--BN068,Liên bang Nga--BN069,Anh--BN070,Anh--BN071,Pháp-BN060-BN072,Anh--BN073,Pháp--BN074,Anh--BN075,Pháp--BN076,Anh--BN077,Anh--BN078,Anh--BN079,Anh--BN080,Pháp--BN081,Anh--BN082,Thổ Nhĩ Kỳ--BN083,Anh--BN084,Anh--BN085,KXD--BN086,-BN086-BN087,Anh--BN088,Nhật Bản--BN089,Tây Ban Nha--BN090,Anh-BN097-BN091,Pháp--BN092,Hungary--BN093,Cộng hòa Séc--BN094,Pháp--BN095,Pháp--BN096,Malaysia--BN097,Malaysia-BN097-BN098,Pháp--BN099,Malaysia--BN100,Anh--BN101,Anh--BN102,Anh--BN103,Anh--BN104,Malaysia--BN105,Malaysia--BN106,-BN086-BN107,Anh--BN108,Anh--BN109,Mỹ--BN110,Anh--BN111,Pháp--BN112,Anh--BN113";
  
  // $.ajax({

  // })
  // var dataInfo;

  testdata = testdata.split(",");
  var convertToIndex =
    "Trung Quốc,Anh,Hàn Quốc,Mỹ,Pháp,Cộng hòa Séc,Tây Ban Nha,Malaysia,Thụy Sĩ,Singapore,Liên bang Nga,Thổ Nhĩ Kỳ,KXD,Nhật Bản,Hungary";
  var dataNetwork = [];
  convertToIndex = convertToIndex.split(",");
  convertToIndex.forEach((item) => {
    var obj = new Object();
    obj["name"] = item;
    obj["value"] = "10";
    obj["children"] = [];
    dataNetwork.push(obj);
  });

  testdata.forEach((e) => {
    let item = e.split("-");
    if (item[0] != "" && find(dataNetwork, item[0])) {
      dataNetwork[convertToIndex.indexOf(item[0])]["children"].push({
        name: item[2],
      });
    } else if (item[1] != "") {
      if (find(dataNetwork, item[1])) {
        dataNetwork = addToData(dataNetwork, item);
      }
    }
  });
  for (var key in dataInfo) {
    if (dataInfo.hasOwnProperty(key)) {
      dataNetwork = addInfoToData(dataNetwork, key, dataInfo[key]);
    }
  }
  addDepthColor(dataNetwork);
  networkSeries.data = dataNetwork;
})()