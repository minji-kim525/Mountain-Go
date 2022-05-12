let y_cen = 37.4981125   // lat
let x_cen = 127.0379399  // long
let map;
let markers = []
let infowindows = []
$(document).ready(function () {
    map = new naver.maps.Map('map', {
        center: new naver.maps.LatLng(y_cen, x_cen),
        zoom: 5,
        zoomControl: true,
        zoomControlOptions: {
            style: naver.maps.ZoomControlStyle.SMALL,
            position: naver.maps.Position.TOP_RIGHT
        }
    });

    get_mountains()
})

setTimeout(function () {
    window.dispatchEvent(new Event('resize'));
}, 600);

function get_mountains() {
    $('#mountain-box').empty();
    markers = []
    infowindows = []
    $.ajax({
        type: "GET",
        url: `/mountain`,
        data: {},
        success: function (response) {
            let mountains = response["mountain_list"]
            for (let i = 0; i < mountains.length; i++) {
                let mountain = mountains[i]
                make_card(i, mountain)
                let marker = make_marker(mountain)
                add_info(i, marker, mountain)
            }
        }
    });
}

function make_marker(mountain) {
    let marker = new naver.maps.Marker({
        position: new naver.maps.LatLng(mountain["mapy"], mountain["mapx"]),
        map: map
    });
    markers.push(marker)
    return marker
}

function make_card(i, mountain) {
    let html_temp =  `<div class="card" id="card-${i}">
                        <div class="card-body">
                        <h5 class="card-title"><a href="#" class="matjip-title">${mountain['name']}</a>⛰</h5>
                        <p class="card-text">${mountain['address']}</p>
                        </div>
                     </div>`;
    $('#mountain-box').append(html_temp);
}

function add_info(i, marker, mountain) {
    let html_temp = `<div class="iw-inner">
						<h5>${mountain['name']}</h5>
						<p>${mountain['address']}
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
    infowindows.push(infowindow)
    naver.maps.Event.addListener(marker, "click", function (e) {
        console.log("clicked", infowindows.length)
        if (infowindow.getMap()) {
            infowindow.close();
        } else {
            infowindow.open(map, marker);
            map.setCenter(infowindow.position)
            $("#mountain-box").animate({
                scrollTop: $("#mountain-box").get(0).scrollTop + $(`#card-${i}`).position().top
            }, 2000);
        }
    });
}

function click2center(i) {
    let marker = markers[i]
    let infowindow = infowindows[i]
    if (infowindow.getMap()) {
        infowindow.close();
    } else {
        infowindow.open(map, marker);
        map.setCenter(infowindow.position)
    }
}


function to_first() {
    window.location.href = "/first"
}



function receive_img() {

    let image_shot = $('#inputGroupFile04').val()

    $.ajax({
        type: "POST",
        url: `/HanLa`,
        data : {'image-0':image_shot},
         success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
}
//
// function save_comment(){
//
//     let name = $('#name').val()
//     let comment = $('#comment').val()
//
//     $.ajax({
//         type: 'POST',
//         url: '/toy',
//         data: {'name_give':name,'comment_give':comment},
//         success: function (response) {
//             alert(response['msg'])
//             window.location.reload()
//         }
//     });
// }