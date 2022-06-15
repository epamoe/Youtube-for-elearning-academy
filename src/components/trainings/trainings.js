import LNavBar from '../global/lNavBar/LNavBar.vue'
import ListDrop from '../global/listDrop/ListDrop.vue'
import LPagination from '../global/lPagination/LPagination.vue'
import InputSearchT from './inputSearchT/InputSearchT.vue'
import LPublication from '../global/lPublication/LPublication.vue'
export default {
  name: 'training',
  components: {
    LNavBar,
    ListDrop,
    InputSearchT,
    LPublication,
    LPagination
  },
  data () {
    return {
      trainings: [{name:1},{name:1},{name:1},{name:1},{name:1},{name:1},{name:1},{name:1}]
    }
  }
}
