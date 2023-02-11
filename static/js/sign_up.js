const loginId = document.getElementById('SIGN_ID');
const loginPw = document.getElementById('SIGN_PW');
const loginBtn = document.getElementById('SIGN_BTN');

function color() {
    if(loginId.value.length>0 && loginPw.value.length>=5){
        loginBtn.style.backgroundColor = "#0095F6";
        loginBtn.disabled = false;
    }else{
        loginBtn.style.backgroundColor = "#C0DFFD";
        loginBtn.disabled = true;
    }
}


loginId.addEventListener('keyup', color);
loginPw.addEventListener('keyup', color);


function signup() {
        $.ajax({
            type: "POST",
            url: "/api/signup",
            data: {
                id_give: $('#SIGN_ID').val(),
                pw_give: $('#SIGN_PW').val(),
                pw_pw_give: $('#SIGN_CHECK').val(),
                nickname_give: $('#NICKNAME').val()
            },
            success: function (response) {
                if (response['result'] == 'success') {
                    alert('회원가입이 완료되었습니다.')
                    window.location.href = '/'
                } else {
                    alert(response['msg'])
                }
            }
        })
    }



