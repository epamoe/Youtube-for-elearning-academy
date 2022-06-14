<template>
    <div class ="lPublication" :style="{display: Display}">
        <div class="lPType">{{ publication_type }}</div>
        <div class="lPImg"><img :src='publication_img' :style="{display:DisplayImg}"/></div>
        <div class="lPDate">
            <div @click="toProfile" class="lPAuthor">
                <div class="lPStars"> <div v-for="(color, index) in star_colors" :key="index"> <LPStar :Color="color.color"/> </div> </div>
                <div><span>{{ publication_author }}</span></div>
            </div>
        </div>
        <div @click="toPublication" class="lPText" :style="{maxHeight:vtext_height}">{{ publication_text }} </div>
        <div class="lPStart"><div>Start</div></div>
    </div>
</template>
<style src="./lPublication.css">
</style>
<script src="./lPublication.js">
</script>
