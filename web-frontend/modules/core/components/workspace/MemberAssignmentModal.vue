<template>
  <Modal :full-height="true" :small="true">
    <MemberSelectionList
      ref="memberSelectionList"
      class="padding-top-2"
      :members="members"
      @invite="storeSelectedMembers"
    />
  </Modal>
</template>

<script>
import Modal from '@fwego/modules/core/mixins/modal'
import MemberSelectionList from '@fwego/modules/core/components/workspace/MemberSelectionList'

export default {
  name: 'MemberAssignmentModal',
  components: { MemberSelectionList },
  mixins: [Modal],
  props: {
    members: {
      type: Array,
      required: true,
    },
  },
  methods: {
    storeSelectedMembers(membersSelected) {
      this.$emit('invite', membersSelected)
      this.hide()
    },
  },
}
</script>
