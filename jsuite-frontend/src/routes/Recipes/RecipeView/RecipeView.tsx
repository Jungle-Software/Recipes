import { useQuery, gql } from "@apollo/client";
import { View } from "./RecipeView.styles";
import DevError from "../../../components/DevError/DevError";
import SelectRecipeError from "./SelectRecipeError/SelectRecipeError";

const RECIPE_BY_ID_QUERY = gql`
  query RecipeView($id: Int!) {
    recipeById(id: $id) {
      title
      description
      portionSize
      prepTime
      cookTime
      ingredients
      instructions
      additionalNotes
      nutritionalInfo
      dateCreated
    }
  }
`;

const RecipeView = (props: any) => {
  const recipeID = props.recipeID;
  const { data, loading, error } = useQuery(RECIPE_BY_ID_QUERY, {
    variables: { id: recipeID },
  });

  if (recipeID === 0) return <SelectRecipeError />;
  if (loading) return <div>"Loading..."</div>;
  if (error) return <DevError />;

  return (
    <View>
      {data.recipeById.title}
      <br />
      {data.recipeById.description}
      <br />
      {data.recipeById.portionSize}
      <br />
      {data.recipeById.prepTime}
      <br />
      {data.recipeById.cookTime}
      <br />
      {data.recipeById.ingredients}
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
