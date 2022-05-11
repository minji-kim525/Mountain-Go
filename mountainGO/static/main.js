let y_cen = 37.4981125;
let x_cen = 127.0379399;
let map;
let markers = [];
let infowindows = [];
$(document).ready(function () {         // 나는 id = map 으로 연결 시킨적이 없지만 네이버가 담당중임 ( head 파일의 오픈api )
    map = new naver.maps.Map('map', {
        center: new naver.maps.LatLng(y_cen, x_cen), // ( 위도 값, 경도 값 )
        zoom: 7,   // 줌을 7 땡겨줘
        zoomControl: true, // 확대 축소 하는 컨트롤 을 켜줘(true)
        zoomControlOptions: {
            style: naver.maps.ZoomControlStyle.SMALL,   // 옵션은 여러 가지 작게 보여주고
            position: naver.maps.Position.TOP_RIGHT     // 오른쪽 위에 보여줘
        }
    });
    get_mountains();

    setTimeout(function () {        // 의문의 지도짤림방지 코드 ..
        window.dispatchEvent(new Event('resize'));
    }, 600);


    naver.maps.Event.addListener(marker, "click", function () { // 네이버 맵에 Event(행동)이 발생했음을 알림
        // addListener : 사용자가 marker에 click 이라는 행동을 했냐 안했냐 귀를 기울이는 녀석
        console.log(infowindow.getMap()); // 정보창이 열려있을 때는 연결된 지도를 반환하고 닫혀있을 때는 null을 반환
        if (infowindow.getMap()) {  // infowindow가 열려 있을때 지도 알림창을 구현하고 열리지 않을때는 null 반환 if문안에서 false 인식
            infowindow.close();
        } else {
            infowindow.open(map, marker);
        }
    });


    function get_mountains() {
        $('#mountain-box').empty();
        $.ajax({
            type: "GET",
            url: '/mountain',
            data: {},
            success: function (response) {
                let mountains = response["mountain_list"]
                for (let i = 0; i < mountains.length; i++) {
                    let mountain = mountains[i]
                    console.log(mountain)
                    make_card(i, mountain);
                    let marker = make_marker(mountain);
                    add_info(i, marker, mountain);
                }
            }
        });
    }

    function make_card(i, mountain) {
        let temp_html = `<div class="card" id="card-${i}">
            <div class="card-body">
                <h5 class="card-title"><a href="#" class="matjip-title">${mountain['name']}</a>⛰</h5>
                <p class="card-text">${mountain.address}</p>
            </div>
           </div>`;
        $('#mountain-box').append(temp_html);
    }


    function make_marker(mountain) {
        let marker = new naver.maps.Marker({
            position: new naver.maps.LatLng(mountain["mapy"], mountain["mapx"]),
            map: map
        });
        markers.push(marker);
        return marker
    }

    function add_info(i, marker, mountain) {
        let html_temp = `<div class="iw-inner">
                        <h5>${mountain['name']}</h5>
                        <p>${mountain['address']}</p>
                        </div>`;
        let infowindow = new naver.maps.InfoWindow({
            content: html_temp,
            maxWidth: 200,
            backgroundColor: "#fff",
            borderColor: "#888",
            borderWidth: 2,
            anchorSize: new naver.maps.Size(15, 15),
            anchorSkew: true,
            anchorColor: "#fff",
            pixelOffset: new naver.maps.Point(10, -10)
        });
        infowindows.push(infowindow);
        naver.maps.Event.addListener(marker, "click", function (e) {
            if (infowindow.getMap()) {
                infowindow.close();
            } else {
                infowindow.open(map, marker);
                map.setCenter(infowindow.position)  // 마커를 누르면 화면 중앙으로 이동
                $("#mountain-box").animate({
                    scrollTop: $("#mountain-box").get(0).scrollTop + $(`#card-${i}`).position().top
                }, 2000); //2000은 2초
            }
        });
    }
})


