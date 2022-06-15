import Slider from './Slider.vue'
export default {
  name: 'lPagination',
  data () {
    return {
      datas1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17], // i should delete that
      datas: [],
      index: 0, // -- the first index amongs index pages visible
      dataIndex: 0, // the current page
      currentElement: [],
      colors: [
        { bg: 'transparent', color: 'inherit' },
        { bg: '#1C8EFB', color: 'white' },
        { bg: 'transparent', color: 'inherit' }
      ],
      reaction: '',
      typeRequest: 'latest'
    }
  },
  components: {
    Slider
  },
  methods: {
    splitTable (table, slice) {
      let i
      let j = 0
      let k = 0
      let max = table.length
      let result = []
      let resultElement = []
      for (i = 0; i < max; i++) {
        j++
        resultElement.push(table[i])
        if (j === slice) {
          k = i
          result.push(resultElement)
          resultElement = []
          j = 0
        }
      }
      // --- ajoutons le reste des éléments
      resultElement = []
      if (max < slice) k = -1
      for (i = k + 1; i < max; i++) {
        resultElement.push(table[i])
      }
      if (resultElement.length > 0) result.push(resultElement)
      return result
    },
    changeIndex (newIndex) {
      this.datasIndex = this.index + newIndex
      this.$parent.$emit('pageChanged', this.datas1[this.index + newIndex])
      this.initializeColor(newIndex)
      this.saveLPagination(newIndex, this.index)
    },
    changeRange (i) {
      let newIndex
      this.index += i * 3
      if (i === 1) newIndex = 0
      else newIndex = 2
      this.initializeColor(newIndex)
      this.$parent.$emit('pageChanged', this.datas1[this.index + newIndex])
      this.datasIndex = this.index + newIndex
      this.saveLPagination(newIndex, this.index)
    },
    initializeColor (current) {
      let i
      for (i = 0; i < 3; i++) {
        this.colors[i].bg = 'transparent'
        this.colors[i].color = 'inherit'
      }
      this.colors[current].bg = '#1C8EFB'
      this.colors[current].color = 'white'
    },
    updateDatas (newIndex, index) {
      this.$root.$emit('loading', 'on')
      const axios = require('axios')
      axios.post(this.$store.state.baseUrl + 'selectPublication.php', {
        reactionType: this.reaction,
        typeRequest: this.typeRequest
      })
        .then((response) => {
          // reinitializing variables
          this.index = index
          this.dataIndex = 0
          this.currentElement = []
          this.currentElement = []
          this.colors = [
            { bg: '#1C8EFB', color: 'white' },
            { bg: 'transparent', color: 'inherit' },
            { bg: 'transparent', color: 'inherit' }
          ]
          // updating
          this.datas1 = this.splitTable(response.data, 8)
          this.$parent.$emit('pageChanged', this.datas1[this.index + newIndex])
          this.initializeColor(newIndex)
          this.$root.$emit('loading', 'off')
        })
        .catch((error) => {
          console.log(error)
          alert(error)
        })
    },
    saveLPagination (newIndex, index) {
      const axios = require('axios')
      axios.post(this.$store.state.baseUrl + 'saveLPagination.php', {
        request: 'save',
        reaction: this.reaction,
        typeRequest: this.typeRequest,
        newIndex: newIndex,
        index: index
      })
        .then((response) => {
        })
        .catch((error) => {
          console.log(error)
          alert(error)
        })
    },
    getLPagination () {
      const axios = require('axios')
      axios.post(this.$store.state.baseUrl + 'saveLPagination.php', {
        request: 'get'
      })
        .then((response) => {
          console.log(response.data)
          this.index = response.data.index
          this.reaction = response.data.reaction
          this.typeRequest = response.data.typeRequest
          this.updateDatas(response.data.newIndex, response.data.index)
        })
        .catch((error) => {
          console.log(error)
          alert(error)
        })
    }
  },
  computed: {
    cPrevious () {
      if (this.index < 3 || this.datas1.length < 1) {
        return 'none'
      }
      return 'block'
    },
    cNext () {
      if (this.index >= this.datas1.length - 3 || this.datas1.length < 1) {
        return 'none'
      }
      return 'block'
    },
    cFirst () {
      if (this.datas1.length < 1 || this.index > this.datas1.length - 1) {
        return 'none'
      }
      return 'block'
    },
    cSecond () {
      if (this.datas1.length < 2 || this.index + 1 > this.datas1.length - 1) {
        return 'none'
      }
      return 'block'
    },
    cThird () {
      if (this.datas1.length < 3 || this.index + 2 > this.datas1.length - 1) {
        return 'none'
      }
      return 'block'
    }
  }
}
