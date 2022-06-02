<template>
<section class="inscription">
    <div class="inscriptionLeft">
        <header>
            <div class="inscriptionLogo">Logo </div>
            <div>Sign up </div>
        </header>
        <div class="insMain">
            <form class = "insMainSection" @submit="submiting" action="#">
                <div class="insLogWith">
                    <div>
                        <div class="insOrangeBut"><img src="./image/google.svg">Log in with google</div>
                    </div>
                    <div class="insButtom1">
                        <div class="insOrangeBut"><img src="./image/facebook.svg">Log in with Facebook</div>
                    </div>
                </div>
                <div class="insLineOr">
                    <div></div><span>Or</span><div></div>
                </div>
                <div style="margin-bottom:30px" class ="insInput">
                    <InputI0 placeholder="Enter your login" name="Login" ref="login" type = "text" pattern="^[a-zA-Z1-9]{4,22}$"/>
                </div>
                <div class ="insInput">
                    <InputI0 placeholder="Enter your password" name="Password" ref="password" type = "password" pattern="^.{4,22}$" />
                </div>
                <div class = "insSetting">
                    <div>
                        <input type="checkbox"> Keep logged in
                     </div>
                    <div class="insButtom1">
                        Forgot password
                    </div>
                </div>
                <div @click='toNext' class="insButtonI0" >SIgn up</div>
                <div style="font-size:12px;text-align:center;margin-top:40px;font-weight:bold" class="loginDont" > Don't registered yet ? 
                    <a style="color:#1C8EFB;" href="register">sign up</a>
                </div>
            </form>
        </div>
    </div>
    <div class="inscriptionRight">
    </div>
    <YAlert ref="yAlert" type="success"/>
    <YAlert ref="yAlertD" type="danger"/>
</section>
</template>
<style src="./inscription.css">
</style>
<script src = "./login.js">
</script>
