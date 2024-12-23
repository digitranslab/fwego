### What is in this MR
- E.g. a short explanation of what this MR does.

### How to test this MR
- E.g. a short series of steps on how to test the features/bug fixes in this MR.

### Merge Request Checklist

- [ ] A changelog entry has been added to `changelog/entries/unreleased` using `changelog/src/changelog.py`
- [ ] New/updated **Premium/Enterprise features** are separated correctly in the premium or enterprise folder
- [ ] The latest **Chrome and Firefox** have been used to test any new frontend features
- [ ] [Documentation](https://github.com/digitranslab/fwego/-/tree/develop/docs) has been
  updated
- [ ] [Quality Standards](https://github.com/digitranslab/fwego/-/blob/develop/CONTRIBUTING.md#quality-standards)
  are met
- [ ] **Performance**: tables are still fast with 100k+ rows, 100+ field tables
- [ ] The [redoc API pages](https://api.fwego.io/api/redoc/) have been updated for any
  REST API changes
- [ ] 
  Our [custom API docs](https://github.com/digitranslab/fwego/-/blob/develop/web-frontend/modules/database/pages/APIDocsDatabase.vue)
  are updated for changes to endpoints accessed via api tokens
- [ ] The UI/UX has been updated
  following [UI Style Guide](https://fwego.io/style-guide)
- [ ] Security impact of change has been considered
