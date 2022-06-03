import Testimony from './testimony/Testimony.vue'
export default {
  name: 'MyProfile',
  components: {
    Testimony
  },
  props: {
    message: String
  },
  methods: {
    move (i) {
      if ((this.position >= -100 && i === -1) || (this.position < 0 && i === 1)) {
        this.position += i * 100
      }
    }
  },
  data () {
    return {
      position: 0
    }
  },
  computed: {
    Position () {
      return this.position + '%'
    }
  }
}
