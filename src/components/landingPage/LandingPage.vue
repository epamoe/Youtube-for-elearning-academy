<template>
  <div class="landingPage">
    <LNavBar />
    <div class="lMain">
      <div class="lMainF">
        <div class="lMainFLeft">
          <span class="lMainTitleBig">A New Way Of Digital Learn</span>
          <span>Loren ipsum dolor sit amet,consectetur adipiscing elit.</span>
          <div>
            <ButtonLand1 message="Get started"/>
            <img src="./img/play.svg"/>
          </div>
        </div>
        <div class="lMainFRight"><span>IMG</span></div>
      </div>
      <div class="lMainSearch">
        <InputSearch/>
      </div>
      <div class="lMainSuggest">
        <div v-for="(sug, index) in sugession" :key="index" class="lMainSButton">
          {{sug.nom}}
        </div>
      </div>
      <div class="lMainTaining">
        <div style="text-align:center">
            <span class="lMainTTitle">Best trainings <img src='./img/curve.svg'/></span>
        </div>
        <div class="lMainTRow">
          <div v-for="(train, index) in trainings.slice(0,4)" :key="index" ><LPublication :data='train'/></div>
        </div>
        <div class="lMainTRow">
          <div v-for="(train, index) in trainings.slice(4,8)" :key="index" ><LPublication :data='train'/></div>
        </div>
      </div>
      <div class="lMainBMember">
        <div><BecomeMember/></div><div><img/></div>
      </div>
      <div class="lMainUserSays">
        <div class="lMainUTitle" style="text-align:right">
            <span class="lMainTTitle">Ours User says <img src='./img/curve.svg'/></span>
        </div>
        <div><MyProfile/></div>
      </div>
      <div class="lMainHereHelp">
        <div><HereHelp/></div><div><img/></div>
      </div>
      <div class="lMainNewlet">
        <NewsLetter/>
      </div>
    </div>
    <LFooter/>
  </div>
</template>
<style src="./landingPage.css">
</style>
<script src="./landingPage.js">
</script>
