import InputI0 from './subComponents/InputI0.vue'
import ButtonI0 from './subComponents/ButtonI0.vue'
import ButtonI1 from './subComponents/ButtonI1.vue'
import FooterI from './subComponents/FooterI.vue'
import YAlert from '../global/yAlert/YAlert.vue'
import axios from 'axios'
export default {
  name: 'inscription',
  components: {
    InputI0,
    ButtonI0,
    ButtonI1,
    FooterI,
    YAlert
  },
  methods: {
    submiting (e) {
      e.preventDefault()
      return false
    },
    toNext () {
      if (this.validation()) {
        /* axios.headers = {'X-Requested-With': 'XMLHttpRequest',
        'accept': 'application/json','Content-Type': 'application/json' }*/
        axios.post(this.$store.state.baseUrl + 'register', {
          login: this.$refs.login.message,
          email: this.$refs.email.message,
          password: this.$refs.password.message,
          confirm_password: this.$refs.confirmpw.message
        })
          .then(() => {
            this.$store.commit('cDisplayCheckmail', true)
            this.$router.push('login')
          })
          .catch((error) => {
            this.$refs.yAlert.display(error.response.data.detail)
            console.log(error)
          }).finally(() => {
            // Perform action in always
          })
      }
    },
    validation () {
      let regex1 = /^.{2,22}$/
      let regex2 = /^.{4,22}$/
      if (!regex1.test(this.$refs.login.message)) {
        this.$refs.yAlert.display('login incorrect')
        return false
      }
      if (!regex2.test(this.$refs.password.message)) {
        this.$refs.yAlert.display('password incorrect')
        return false
      }
      if (this.$refs.password.message !== this.$refs.confirmpw.message) {
        this.$refs.yAlert.display('passwords did not match')
        return false
      }
      return true
    }
  }
}

