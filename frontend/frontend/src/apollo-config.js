import {
  ApolloClient,
  ApolloLink,
  createHttpLink,
  InMemoryCache,
} from "@apollo/client/core";
import { createApolloProvider } from "@vue/apollo-option";
import { setContext } from "@apollo/client/link/context";

// proper way of importing createUploadLink
// https://github.com/jaydenseric/apollo-upload-client/blob/master/createUploadLink.mjs
import createUploadLink from "apollo-upload-client/createUploadLink.mjs";

const httpLink = createUploadLink({
  uri: import.meta.env.VITE_BACKEND_SERVER + "/graphql",
});
// const httpLink = createHttpLink({
//   uri: "http://127.0.0.1:8000/graphql",
//   // uri: "http://localhost:8000/graphql",
// });

const authLink = setContext((_, { headers }) => {
  // get the authentication token from local storage if it exists
  const token = localStorage.getItem("token");
  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : "",
    },
  };
});

export const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache(),
});

// export const apolloClient = new ApolloClient({
//   link: authLink.concat(ApolloLink.from([
//     createUploadLink({
//       uri: "http://127.0.0.1:8000/graphql",
//     })
//   ])),
//   cache: new InMemoryCache(),
// });

export const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
});
