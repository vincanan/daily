
       //오늘 날짜값 불러오기
        window.onload = function() {
		today = new Date();
		console.log("today.toISOString() >>>" + today.toISOString());
		today = today.toISOString().slice(0, 10);
		console.log("today >>>> " + today);
		bir = document.getElementById("datepicker");
		bir.value = today;
        show_daily()
	    }


       $(document).ready(function() {
        $('#datepicker').on('input', (event) => show_daily());
        });



    // Daily 등록
    function check_daily() {
        let user = 'junz';
        let date = $('#datepicker').val();
        let comment = $('#daily_com').val();



        if(comment == ''){
            alert('내용을 입력해주세요!')
        }else {
            $.ajax({
                type: 'POST',
                url: '/daily',
                data: {user_give: user, date_give: date, comment_give: comment},
                success: function (response) {
                    alert(response['msg'])
                    window.location.reload()
                }
            });
        }
    }


    function show_daily() {
        $('#daily-list').empty();

        $.ajax({
            type: "GET",
            url: "/daily",
            data: {},
            success: function (response) {
                let rows = response['comments']
                for (let i = 0; i < rows.length; i++) {
                    let num = rows[i]['num']
                    let date = rows[i]['date']
                    let user = rows[i]['user']
                    let comment = rows[i]['comment']
                    let done = rows[i]['done']

                    let temp_html = ``
                    const now_date = $('#datepicker').val();
                    const user_id = 'junz';
                    if (user == user_id && date == now_date) {
                        if (done == 0) {
                            temp_html = `
                                <li>
                                    <h2>✨ ${comment}</h2>
                                    <button onclick="done_comment(${num})" type="button" class="btn btn-outline-primary">완료!</button>
                                </li>
                            `
                        } else {
                            temp_html = `
                                <li>
                                    <h2>✅ ${comment}</h2>
                                    <button type="button" onclick="cancel_bucket(${num})" type="button" class="btn btn-outline-danger">취소</button>
                                </li>
                            `
                        }

                        $('#daily-list').append(temp_html)

                    }
                }
            }
        });
    }
