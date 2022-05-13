<template>
    <div class="grid gap-5 grid-cols-12">
        <div class="col-span-8">
            <Video></Video>
        </div>
        <div class="col-span-4 w-full content">
           <Content></Content> 
        </div>
    </div>
</template>

<script>
    import Video from "./Video.vue"
    import Content from "./Content.vue"

    export default {
        components: {
            Video,
            Content,
        }
    }
</script>

<style>
    .content{
        background: #EDEDED;
    }
</style>