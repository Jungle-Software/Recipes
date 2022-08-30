import { useQuery, gql } from "@apollo/client";
import { View, Prompt } from "./RecipeView.styles";
import DevError from "../../../components/DevError/DevError";

export const RECIPE_BY_ID_QUERY = gql`
  query RecipeById($id: Int!) {
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
  const recipeID = props.recipeId;
  const { data, loading, error } = useQuery(RECIPE_BY_ID_QUERY, {
    variables: { id: recipeID },
  });

  if (recipeID === 0) return <Prompt id="select-recipe-prompt">Please select a recipe (or insert a new one if you have none!)</Prompt>;
  if (loading) return <div>"Loading..."</div>;
  if (error) return <DevError />;

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
