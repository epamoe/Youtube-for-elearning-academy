import axios from 'axios'
export default {
  name: 'InputSearch',
  data () {
    return {
      toSearch: ''
    }
  },
  methods: {
    search () {
      alert('sds')
      axios.get(this.$store.state.baseUrl + 'landing/search', {
        query: this.toSearch,
      })
        .then((response) => {
          console.log(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
