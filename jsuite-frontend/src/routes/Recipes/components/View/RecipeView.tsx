import { View } from "./RecipeView.styles";

const RecipeView = (props: any) => {
  // TODO might want to find a better way to handle this than adding a default empty recipe
  const recipe = props.recipe
    ? props.recipe
    : {
        id: -1,
        title: "",
        description: "",
        portionSize: 0,
        prepTime: 0,
        cookTime: 0,
        ingredients: "",
        instructions: "",
        additionalNotes: "",
        nutritionalInfo: "",
      };

  // TODO handle actual empty graphql query in view

  return (
    <View>
      {recipe.id}

      {recipe.title}

      {recipe.description}

      {recipe.portionSize}

      {recipe.prepTime}

      {recipe.cookTime}

      {recipe.ingredients}

      {recipe.instructions}

      {recipe.additionalNotes}

      {recipe.nutritionalInfo}

      {recipe.dateCreated}
    </View>
  );
};

export default RecipeView;
