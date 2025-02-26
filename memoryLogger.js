module.exports = function memoryLoggerPlugin() {
  return {
    name: 'memory-logger-plugin',
    async loadContent() {
      console.log('Initial Memory Usage:', process.memoryUsage());
    },
    async contentLoaded({content, actions}) {
      console.log('After Content Loaded:', process.memoryUsage());
    },
    async postBuild(props) {
      console.log('After Build:', process.memoryUsage());
    },
  };
};