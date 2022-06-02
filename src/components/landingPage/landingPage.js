import InputSearch from '../global/inputSearch/InputSearch.vue'
import LNavBar from '../global/lNavBar/LNavBar.vue'
import LFooter from '../global/lFooter/LFooter.vue'
import LPublication from '../global/lPublication/LPublication.vue'
import BecomeMember from '../global/becomeMember/BecomeMember.vue'
import HereHelp from '../global/becomeMember/HereHelp.vue'
import MyProfile from '../global/myProfile/MyProfile.vue'
import NewsLetter from '../global/newsLetter/NewsLetter.vue'
import ButtonLand1 from './ButtonLand1.vue'
export default {
  name: 'landingPage',
  components: {
    InputSearch,
    LNavBar,
    ButtonLand1,
    LFooter,
    LPublication,
    BecomeMember,
    MyProfile,
    HereHelp,
    NewsLetter
  },
  data () {
    return {
      sugession: [{nom:'Javascript developmen'},{nom:'Python'},{nom:'Devops praticises'},{nom:'Android'},{nom:'Scrum methodology'},{nom:'Angular'},
      {nom:'Javascript developmen'},{nom:'Python'},{nom:'Devops praticises'},{nom:'Android'},{nom:'Scrum methodology'},
      {nom:'Javascript developmen'},{nom:'Python'},{nom:'Devops praticises'},{nom:'Android'},{nom:'Scrum methodology'},{nom:'Angular'}],
      
      trainings: [{name:1},{name:1},{name:1},{name:1},{name:1},{name:1},{name:1},{name:1}]
    }
  }
}
