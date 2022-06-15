export default {
  name: 'listDrop',
  data () {
    return {
      all: {name:"All",selected:'#1C8EFB'},
      categories: [{name:'FrontEnd', numb:50, selected:'rgb(40,40,40)'}, 
      {name:'BackEnd', numb:30, selected:'rgb(40,40,40)'}
      ,{name:'Mobile', numb:10, selected:'rgb(40,40,40)'}, 
      {name:'DevOps',numb:"05",selected:'rgb(40,40,40)'},
      {name:'Progamming languages', numb: 10,selected:'rgb(40,40,40)'}],
      current: {name:"All",selected:'#1C8EFB'},
      Display: 'none'
    }
  },
  methods: {
    displaying (){
      this.Display = this.Display == 'none' ? 'block' : 'none'
    },
    select(selected) { 
      this.current = selected
      this.displaying()
    }
  },
  mounted () {
    this.current = this.all
    this.$watch('current',(newVal, oldVal) => {
      oldVal.selected = 'rgb(40,40,40)'
      newVal.selected = '#1C8EFB'
    })
  }
}
