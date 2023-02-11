
       //오늘 날짜값 불러오기

        window.onload = function() {
		today = new Date();
		console.log("today.toISOString() >>>" + today.toISOString());
		today = today.toISOString().slice(0, 10);
		console.log("today >>>> " + today);
		bir = document.getElementById("datepicker");
		bir.value = today;
        show_daily()
        show_todo()
        show_study()
	    }


//daily

       $(document).ready(function () {
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
                    show_daily()
                }
            });
        }
    }

    // Daily 출력
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
                                <li class="comment_wrap">
                                    <h2>✨ ${comment}</h2>
                                    <button onclick="done_daily(${num})" type="button" class="btn btn-outline-primary">완료!</button>
                                </li>
                            `
                        } else {
                            temp_html = `
                                <li class="comment_wrap">
                                    <h2>✅ ${comment}</h2>
                                    <button type="button" onclick="cancel_daily(${num})" type="button" class="btn btn-outline-danger">취소</button>
                                </li>
                            `
                        }

                        $('#daily-list').append(temp_html)

                    }
                }
            }
        });
    }

     function done_daily(num) {
            $.ajax({
                type: "POST",
                url: "/daily/done",
                data: {num_give: num},
                success: function (response) {
                    alert(response["msg"])
                    show_daily()
                }
            });
        }

        function cancel_daily(num){
            $.ajax({
                type: "POST",
                url: "/daily/cancel",
                data: {num_give: num},
                success: function (response) {
                    alert(response["msg"])
                   show_daily()
                }
            });

        }

     // to-do 영역
       $(document).ready(function() {
        $('#datepicker').on('input', (event) => show_todo());
        });

    // to-do 등록
    function check_todo() {
        let user = 'junz';
        let date = $('#datepicker').val();
        let comment = $('#todo_com').val();

        if(comment == ''){
            alert('내용을 입력해주세요!')
        }else {
            $.ajax({
                type: 'POST',
                url: '/todo',
                data: {user_give: user, date_give: date, comment_give: comment},
                success: function (response) {
                    alert(response['msg'])
                    show_todo()
                }
            });
        }
    }

    // to-do 출력
    function show_todo() {
        $('#todo-list').empty();

        $.ajax({
            type: "GET",
            url: "/todo",
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
                                <li class="comment_wrap">
                                    <h2>✨ ${comment}</h2>
                                    <button onclick="done_todo(${num})" type="button" class="btn btn-outline-primary">완료!</button>
                                </li>
                            `
                        } else {
                            temp_html = `
                                <li class="comment_wrap">
                                    <h2>✅ ${comment}</h2>
                                    <button type="button" onclick="cancel_todo(${num})" type="button" class="btn btn-outline-danger">취소</button>
                                </li>
                            `
                        }

                        $('#todo-list').append(temp_html)

                    }
                }
            }
        });
    }

     function done_todo(num) {
            $.ajax({
                type: "POST",
                url: "/todo/done",
                data: {num_give: num},
                success: function (response) {
                    alert(response["msg"])
                   show_todo()
                }
            });
        }

        function cancel_todo(num){
            $.ajax({
                type: "POST",
                url: "/todo/cancel",
                data: {num_give: num},
                success: function (response) {
                    alert(response["msg"])
                    show_todo()
                }
            });

        }

     // study 영역
       $(document).ready(function() {
        $('#datepicker').on('input', (event) => show_study());
        });

    // study 등록
    function check_study() {
        let user = 'junz';
        let date = $('#datepicker').val();
        let comment = $('#study_com').val();

        if(comment == ''){
            alert('내용을 입력해주세요!')
        }else {
            $.ajax({
                type: 'POST',
                url: '/study',
                data: {user_give: user, date_give: date, comment_give: comment},
                success: function (response) {
                    alert(response['msg'])
                    show_study()
                }
            });
        }
    }

    // study 출력
    function show_study() {
        $('#study-list').empty();

        $.ajax({
            type: "GET",
            url: "/study",
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
                                <li class="comment_wrap">
                                    <h2>✨ ${comment}</h2>
                                    <button onclick="done_study(${num})" type="button" class="btn btn-outline-primary">완료!</button>
                                </li>
                            `
                        } else {
                            temp_html = `
                                <li class="comment_wrap">
                                    <h2>✅ ${comment}</h2>
                                    <button type="button" onclick="cancel_study(${num})" type="button" class="btn btn-outline-danger">취소</button>
                                </li>
                            `
                        }

                        $('#study-list').append(temp_html)

                    }
                }
            }
        });
    }
     function done_study(num) {
            $.ajax({
                type: "POST",
                url: "/study/done",
                data: {num_give: num},
                success: function (response) {
                    alert(response["msg"])
                   show_study()
                }
            });
        }

        function cancel_study(num){
            $.ajax({
                type: "POST",
                url: "/study/cancel",
                data: {num_give: num},
                success: function (response) {
                    alert(response["msg"])
                    show_study()
                }
            });

        }


        $.ajax({
            type: "GET",
            url: "https://api.adviceslip.com/advice",
            data: {},
            success: function (advice) {

                const object = JSON.parse(advice);
                let temp_html = object['slip']['advice'];
                $('#wise').append(temp_html);

            }
        })

        $.ajax({
            type: "GET",
            url: "http://api.weatherapi.com/v1/current.json?key=76c676214eee4fc089552024231102&q=Seoul&aqi=yes",
            data: {},
            success: function (weather) {
                let city = weather['location']['name']
                let temp = weather['current']['temp_c']
                let mode = weather['current']['condition']['text']
                $('#weather').append(city,temp,mode);


            }
        })



