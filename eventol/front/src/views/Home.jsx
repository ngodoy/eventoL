import React from 'react'
import {render} from 'react-dom'
import Home from '../containers/Home'
import {Provider} from 'react-redux'
import eventsStore from '../store/eventsStore'
import './index.scss';

const store = eventsStore();
window.render_components = properties => {
  window.params = {...properties};
  render(
    (<Provider store={store}>
      <Home
        background={properties.background}
        eventolMessage={properties.message}
        logoHeader={properties.logo_header}
        logoLanding={properties.logo_landing}
        user={properties.user}
      />
    </Provider>), document.getElementById('root'));
};

if (module.hot) {
  if (window.params) window.render_components(window.params);
  module.hot.accept();
}
