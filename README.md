# Example Application for using Ariadne and Flask

## Setup

Run application with 

```
flask run
```

Introspection / GrapiQL

http://localhost:5000/graphql

## Examples

**Query all posts**

```graphql
query AllPosts {
  listPosts {
    success
    errors
    post {
      id
      title 
      description
      created_at
    }
  }
}
```

**Query post by id**

```graphql
query GetPost {
  getPost(id: "1") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}
```

**Create a new post**

```graphql
mutation CreateNewPost {
  createPost(
    title: "New Blog Post", 
    description:"Some Description") {
    post {
      id
      title
      description
      created_at
    }
    success
    errors
  }
}
```

**Update an existing post**

```graphql
mutation UpdatePost {
  updatePost(id:"2", title:"Hello title", description:"updated description") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}
```

**Delete a post**

```graphql
mutation DeletePost {
  deletePost(id:"2") {
    success
    errors    
    post {
      id
      title
      description
    }
  }
}
```
