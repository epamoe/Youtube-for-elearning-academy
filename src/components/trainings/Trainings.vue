<template>
    <div class="trainings">
        <LNavBar/>
        <div class="trgsMenu">
            <div class="trgsMenuFirst">
                <span>Categories:</span>
                <ListDrop/>
            </div>
            <div>
                <InputSearchT/>
            </div>
        </div>
        <div class="trgsTaining" style="z-index:0">
            <div class="trgsTRow">
                <div v-for="(train, index) in trainings.slice(0,4)" :key="index" ><LPublication :data='train'/></div>
            </div>
            <div class="trgsTRow">
                <div v-for="(train, index) in trainings.slice(4,8)" :key="index" ><LPublication :data='train'/></div>
            </div>
        </div>
        <div class="tgrsPagination">
            <LPagination/>
        </div>
    </div>
</template>
<style src="./trainings.css">
</style>
<script src = "./trainings.js">
</script>
