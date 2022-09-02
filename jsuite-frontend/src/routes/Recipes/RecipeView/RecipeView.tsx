import { useQuery, gql } from "@apollo/client";
import { View, Prompt } from "./RecipeView.styles";
import DevError from "../../../components/DevError/DevError";
import { SELECT_RECIPE_PROMPT } from "../../../constants";
import LoadingMessage from "../../../components/LoadingMessage/LoadingMessage";

export const RECIPE_BY_ID_QUERY = gql`
  query RecipeById($id: ID!) {
    recipeById(id: $id) {
      title
      description
      categories{
        name
      }
      portionSize
      prepTime
      cookTime
      ingredients{
        name
        allergens{
            type
        }
      }
      instructions
      additionalNotes
      nutritionalInfo
      dateCreated
    }
  }
`;

type Props = {
  recipeId: number
}

const RecipeView = (props: Props) => {
  const recipeId = props.recipeId;
  const { data, loading, error } = useQuery(RECIPE_BY_ID_QUERY, {
    variables: { id: recipeId },
  });

  if (recipeId === 0) return <Prompt id="select-recipe-prompt">{SELECT_RECIPE_PROMPT}</Prompt>;
  if (loading) return <LoadingMessage />;
  if (error) return <DevError message={error.message}/>;

  return (
    <View id="recipe-view">
      {data.recipeById.title}
      <br />
      {data.recipeById.description}
      <br />
      {data.recipeById.categories[0].name} {/*TEMPORARY FOR TESTING*/}
      <br />
      {data.recipeById.portionSize}
      <br />
      {data.recipeById.prepTime}
      <br />
      {data.recipeById.cookTime}
      <br />
      {data.recipeById.ingredients[0].name} {/*TEMPORARY FOR TESTING*/}
      <br />
      {data.recipeById.ingredients[0].allergens[0].type} {/*TEMPORARY FOR TESTING*/}
      <br />
      {data.recipeById.instructions}
      <br />
      {data.recipeById.additionalNotes}
      <br />
      {data.recipeById.nutritionalInfo}
      <br />
      {data.recipeById.dateCreated}
    </View>
  );
};

export default RecipeView;
