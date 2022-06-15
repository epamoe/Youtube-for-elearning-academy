<template>
    <div class ="lPublication" :style="{display: Display}">
        <div class="lPType">{{ datas.author_login }}</div>
        <div class="lPImg"><img :src='datas.thumbnail' :style="{display:DisplayImg}"/></div>
        <div class="lPDate">
            <div @click="toProfile" class="lPAuthor">
                <div class="lPStars"> <div v-for="(color, index) in star_colors" :key="index"> <LPStar :Color="color.color"/> </div> </div>
                <div><span>{{ datas.title }}</span></div>
            </div>
        </div>
        <div @click="toPublication" class="lPText" :style="{maxHeight:vtext_height}">{{ datas.description }} </div>
        <div class="lPStart"><div>Start</div></div>
    </div>
</template>
<style src="./lPublication.css">
</style>
<script src="./lPublication.js">
</script>
