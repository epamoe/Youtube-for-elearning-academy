import LPStar from './LPStar.vue'
export default {
  name: 'lPublication',
  props: {
    reference: String,
    id: Number,
    datas: {}
  },
  components: {
    LPStar
  },
  data () {
    return {
      publication_type: 'football',
      auth_img: '',
      auth_id: 20,
      // publication_img: './images/dembouz.jpg',
      publication_img: 'http://localhost/projet/datas/pulication_img/image.jpg',
      publication_date: 'MER. 20.02.2000 ',
      publication_author: 'Javascript advance course',
      publication_title: 'The LaLiga Experience serves up one of the matches of the season',
      publication_text: 'Particularly for the special guests of the second LaLiga Experience 2021/22, who got to enjoy one of the most spectacular games of the year',
      publi_numb_com: 100,
      publication_point: 1000,
      // ------ other --------
      Display: 'block',
      DisplayImg: 'block',
      vtext_height: '53px',
      vdisplay_more: 'flex',
      full_text_visible: false,
      star_colors: [{ color: '#FDAA07' },{ color: '#FDAA07' },{ color: '#FDAA07' },{ color: '#FDAA07' },{ color: 'transparent' }],
      react: 'handshake'
    }
  },
  methods: {
    slideText () {
      if (!this.full_text_visible) {
        this.vtext_height = '500px'
      } else {
        this.vtext_height = '53px'
      }
      this.full_text_visible = !this.full_text_visible
    },
    moreVisible (text) {
      if (text > 300) {
        this.vdisplay_more = 'flex'
        this.vtext_height = '53px'
      } else {
        this.vdisplay_more = 'none'
        this.vtext_height = '500px'
      }
    },
    toPublication () {
      this.$router.push({name: 'publication', params: { id: this.id, com: 1, comOfCom: 1 }})
    },
    toProfile () {
      this.$store.commit('updateProfilePage', this.auth_id)
      this.$router.push('profilePage')
    },
    numberStart (a) {
      return a%5
    }
  }, 
}
