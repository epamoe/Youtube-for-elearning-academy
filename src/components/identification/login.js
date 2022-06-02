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
        var params = new URLSearchParams();
        params.append('username', this.$refs.login.message)
        params.append('password', this.$refs.password.message)
        axios.post(this.$store.state.baseUrl + 'login', params)
          .then((response) => {
            console.log(response.data)
            this.$store.commit('setUser', response.data)
            console.log(this.$store.state.login)
            this.$router.push({name: 'MemberDashboard'})
          })
          .catch((error) => {
            this.$refs.yAlertD.display(error.response.data.detail)
            console.log(error)
          })
      }
    },
    validation () {
      let regex1 = /^.{2,22}$/
      let regex2 = /^.{4,22}$/
      if (!regex1.test(this.$refs.login.message)) {
        this.$refs.yAlertD.display('login incorrect')
        return false
      }
      if (!regex2.test(this.$refs.password.message)) {
        this.$refs.yAlertD.display('password incorrect')
        return false
      }
      return true
    }
  },
  mounted () {
    if (this.$store.state.displayCheckEmail) {
      this.$refs.yAlert.display('check your mail account to activate your account')
      this.$store.commit('cDisplayCheckmail', false)
    }
  }
}

